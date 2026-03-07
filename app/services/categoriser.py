"""Transaction categorisation engine.

Uses keyword matching with confidence scoring to auto-categorise bank transactions
into SA103F tax categories. Designed to be replaced/augmented with LLM-based
categorisation as the product matures.
"""

import re
from dataclasses import dataclass

from app.models.transaction import SA103Category, TransactionType


@dataclass
class CategoryMatch:
    category: SA103Category
    confidence: float
    transaction_type: TransactionType


# Keyword rules: (pattern, category, transaction_type, base_confidence)
# Patterns are matched case-insensitively against transaction descriptions.
_RULES: list[tuple[str, SA103Category, TransactionType, float]] = [
    # Income signals
    (r"invoice|payment received|client payment|freelance", SA103Category.TURNOVER, TransactionType.INCOME, 0.75),
    (r"bacs credit|faster payment in|bank giro credit", SA103Category.TURNOVER, TransactionType.INCOME, 0.60),

    # Travel (Box 20)
    (r"trainline|national rail|tfl|oyster|uber|lyft|bolt|taxi|parking|motorway|petrol|diesel|fuel|shell|bp|esso",
     SA103Category.TRAVEL, TransactionType.EXPENSE, 0.80),
    (r"hotel|airbnb|booking\.com|premier inn|travelodge|holiday inn",
     SA103Category.TRAVEL, TransactionType.EXPENSE, 0.70),
    (r"easyjet|ryanair|british airways|flights",
     SA103Category.TRAVEL, TransactionType.EXPENSE, 0.65),

    # Office costs (Box 23)
    (r"amazon|argos|staples|ryman|office depot|stationery",
     SA103Category.OFFICE_COSTS, TransactionType.EXPENSE, 0.55),
    (r"vodafone|ee|three|o2|giffgaff|mobile|broadband|bt|sky|virgin media|plusnet",
     SA103Category.OFFICE_COSTS, TransactionType.EXPENSE, 0.70),
    (r"microsoft|google workspace|slack|zoom|notion|figma|github|gitlab|heroku|aws|azure|digitalocean|netlify|vercel",
     SA103Category.OFFICE_COSTS, TransactionType.EXPENSE, 0.85),
    (r"adobe|canva|mailchimp|hubspot",
     SA103Category.OFFICE_COSTS, TransactionType.EXPENSE, 0.70),
    (r"royal mail|parcelforce|dpd|hermes|evri|postage",
     SA103Category.OFFICE_COSTS, TransactionType.EXPENSE, 0.75),

    # Advertising (Box 24)
    (r"facebook ads|google ads|linkedin ads|twitter ads|instagram ads|tiktok ads|meta ads",
     SA103Category.ADVERTISING, TransactionType.EXPENSE, 0.90),
    (r"advertising|marketing|seo|ppc|sponsorship",
     SA103Category.ADVERTISING, TransactionType.EXPENSE, 0.75),
    (r"squarespace|wix|wordpress|domain|hosting|namecheap|godaddy|cloudflare",
     SA103Category.ADVERTISING, TransactionType.EXPENSE, 0.65),

    # Staff costs (Box 19)
    (r"salary|wages|payroll|pension contribution|employer nic",
     SA103Category.STAFF_COSTS, TransactionType.EXPENSE, 0.85),
    (r"freelancer\.com|upwork|fiverr|peopleperhour|subcontractor",
     SA103Category.STAFF_COSTS, TransactionType.EXPENSE, 0.70),

    # Premises (Box 21)
    (r"rent|rates|council tax|water rates|electricity|gas|utility|utilities",
     SA103Category.PREMISES, TransactionType.EXPENSE, 0.65),
    (r"office rent|coworking|wework|regus",
     SA103Category.PREMISES, TransactionType.EXPENSE, 0.85),

    # Repairs (Box 22)
    (r"repair|maintenance|plumber|electrician|decorator|cleaning",
     SA103Category.REPAIRS, TransactionType.EXPENSE, 0.70),

    # Financial charges (Box 26)
    (r"bank charge|bank fee|card fee|overdraft|stripe fee|paypal fee|transaction fee",
     SA103Category.FINANCIAL_CHARGES, TransactionType.EXPENSE, 0.85),

    # Loan interest (Box 25)
    (r"loan interest|mortgage interest|interest charge",
     SA103Category.LOAN_INTEREST, TransactionType.EXPENSE, 0.80),

    # Cost of goods (Box 17)
    (r"stock|inventory|raw materials|wholesale|supplier|materials",
     SA103Category.COST_OF_GOODS, TransactionType.EXPENSE, 0.60),

    # Professional subscriptions / Other (Box 29)
    (r"subscription|membership|professional body|ipse|fsb|acca",
     SA103Category.OTHER_EXPENSES, TransactionType.EXPENSE, 0.65),
    (r"insurance|professional indemnity|public liability",
     SA103Category.OTHER_EXPENSES, TransactionType.EXPENSE, 0.70),
    (r"accountant|accounting|bookkeeping|tax advice|legal fees|solicitor",
     SA103Category.OTHER_EXPENSES, TransactionType.EXPENSE, 0.75),
    (r"training|course|conference|seminar|cpd",
     SA103Category.OTHER_EXPENSES, TransactionType.EXPENSE, 0.65),
]

# Compiled patterns for performance
_COMPILED_RULES = [
    (re.compile(pattern, re.IGNORECASE), cat, txn_type, conf)
    for pattern, cat, txn_type, conf in _RULES
]


def categorise_transaction(description: str, amount: float) -> CategoryMatch:
    """Categorise a bank transaction based on its description and amount.

    Returns the best matching category with a confidence score.
    Positive amounts are treated as income, negative as expenses.
    """
    # Simple heuristic: positive = income, negative = expense
    is_credit = amount > 0

    best_match: CategoryMatch | None = None
    best_confidence = 0.0

    for pattern, category, txn_type, base_confidence in _COMPILED_RULES:
        # Skip if direction doesn't match
        if is_credit and txn_type == TransactionType.EXPENSE:
            continue
        if not is_credit and txn_type == TransactionType.INCOME:
            continue

        match = pattern.search(description)
        if match:
            # Boost confidence if the match covers a larger portion of the description
            match_ratio = len(match.group()) / max(len(description), 1)
            confidence = min(base_confidence + (match_ratio * 0.15), 0.99)

            if confidence > best_confidence:
                best_confidence = confidence
                best_match = CategoryMatch(
                    category=category,
                    confidence=round(confidence, 2),
                    transaction_type=txn_type,
                )

    if best_match:
        return best_match

    # Default: uncategorised
    return CategoryMatch(
        category=SA103Category.UNCATEGORISED,
        confidence=0.0,
        transaction_type=TransactionType.INCOME if is_credit else TransactionType.EXPENSE,
    )


def categorise_batch(
    transactions: list[tuple[str, float]],
) -> list[CategoryMatch]:
    """Categorise a batch of transactions. Each item is (description, amount)."""
    return [categorise_transaction(desc, amt) for desc, amt in transactions]
