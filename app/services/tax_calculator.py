"""UK tax calculation engine for sole traders / freelancers.

Computes income tax, National Insurance (Class 2 & 4), and provides
real-time estimates of tax liability based on running profit.
"""

from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

# ── 2025/26 Tax Constants ──────────────────────────────────────────────
# These should be updated annually or loaded from config.

PERSONAL_ALLOWANCE = Decimal("12570")
PERSONAL_ALLOWANCE_TAPER_THRESHOLD = Decimal("100000")

BASIC_RATE_LIMIT = Decimal("37700")  # taxable income up to this
HIGHER_RATE_LIMIT = Decimal("125140")  # taxable income up to this

BASIC_RATE = Decimal("0.20")
HIGHER_RATE = Decimal("0.40")
ADDITIONAL_RATE = Decimal("0.45")

# Class 2 NIC
CLASS_2_WEEKLY_RATE = Decimal("3.45")
CLASS_2_WEEKS_PER_YEAR = 52
CLASS_2_SMALL_PROFITS_THRESHOLD = Decimal("6725")

# Class 4 NIC
CLASS_4_LOWER_LIMIT = Decimal("12570")
CLASS_4_UPPER_LIMIT = Decimal("50270")
CLASS_4_MAIN_RATE = Decimal("0.06")  # 6% (reduced from 9% in Jan 2024)
CLASS_4_ADDITIONAL_RATE = Decimal("0.02")

# Home office flat rates (monthly)
HOME_OFFICE_RATES: list[tuple[int, Decimal]] = [
    (101, Decimal("26")),  # 101+ hours/month
    (51, Decimal("18")),   # 51-100 hours/month
    (25, Decimal("10")),   # 25-50 hours/month
]

# Mileage rates
MILEAGE_RATE_FIRST_10K = Decimal("0.45")
MILEAGE_RATE_AFTER_10K = Decimal("0.25")

# VAT threshold
VAT_REGISTRATION_THRESHOLD = Decimal("90000")


def _round_tax(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


@dataclass
class TaxBreakdown:
    """Full tax breakdown for a sole trader."""

    gross_income: Decimal
    total_expenses: Decimal
    net_profit: Decimal

    personal_allowance: Decimal
    taxable_income: Decimal

    basic_rate_tax: Decimal
    higher_rate_tax: Decimal
    additional_rate_tax: Decimal
    total_income_tax: Decimal

    class_2_nic: Decimal
    class_4_nic: Decimal
    total_nic: Decimal

    total_tax_due: Decimal

    effective_rate: Decimal  # percentage

    # Advisory
    approaching_vat_threshold: bool
    suggested_monthly_set_aside: Decimal


def calculate_personal_allowance(gross_income: Decimal) -> Decimal:
    """Personal allowance tapers by £1 for every £2 earned above £100,000."""
    if gross_income <= PERSONAL_ALLOWANCE_TAPER_THRESHOLD:
        return PERSONAL_ALLOWANCE

    reduction = (gross_income - PERSONAL_ALLOWANCE_TAPER_THRESHOLD) / 2
    reduced = PERSONAL_ALLOWANCE - reduction
    return max(reduced, Decimal("0"))


def calculate_income_tax(taxable_income: Decimal) -> tuple[Decimal, Decimal, Decimal]:
    """Calculate income tax split across basic, higher, and additional rate bands."""
    if taxable_income <= 0:
        z = Decimal("0")
        return z, z, z

    basic = min(taxable_income, BASIC_RATE_LIMIT) * BASIC_RATE
    higher = Decimal("0")
    additional = Decimal("0")

    if taxable_income > BASIC_RATE_LIMIT:
        higher_portion = min(taxable_income - BASIC_RATE_LIMIT, HIGHER_RATE_LIMIT - BASIC_RATE_LIMIT)
        higher = higher_portion * HIGHER_RATE

    if taxable_income > HIGHER_RATE_LIMIT:
        additional_portion = taxable_income - HIGHER_RATE_LIMIT
        additional = additional_portion * ADDITIONAL_RATE

    return _round_tax(basic), _round_tax(higher), _round_tax(additional)


def calculate_class_2_nic(net_profit: Decimal) -> Decimal:
    """Class 2 NIC — flat weekly rate if profit exceeds small profits threshold."""
    if net_profit < CLASS_2_SMALL_PROFITS_THRESHOLD:
        return Decimal("0")
    return _round_tax(CLASS_2_WEEKLY_RATE * CLASS_2_WEEKS_PER_YEAR)


def calculate_class_4_nic(net_profit: Decimal) -> Decimal:
    """Class 4 NIC — percentage of profits between lower and upper limits."""
    if net_profit <= CLASS_4_LOWER_LIMIT:
        return Decimal("0")

    main_band = min(net_profit, CLASS_4_UPPER_LIMIT) - CLASS_4_LOWER_LIMIT
    main_nic = main_band * CLASS_4_MAIN_RATE

    additional_nic = Decimal("0")
    if net_profit > CLASS_4_UPPER_LIMIT:
        additional_nic = (net_profit - CLASS_4_UPPER_LIMIT) * CLASS_4_ADDITIONAL_RATE

    return _round_tax(main_nic + additional_nic)


def calculate_home_office_deduction(hours_per_month: int, months: int = 12) -> Decimal:
    """Calculate home office flat-rate deduction based on monthly hours worked from home."""
    for threshold, rate in HOME_OFFICE_RATES:
        if hours_per_month >= threshold:
            return rate * months
    return Decimal("0")


def calculate_mileage_deduction(business_miles: int) -> Decimal:
    """Calculate mileage deduction using HMRC simplified rates."""
    if business_miles <= 10_000:
        return _round_tax(Decimal(business_miles) * MILEAGE_RATE_FIRST_10K)
    first_10k = Decimal("10000") * MILEAGE_RATE_FIRST_10K
    remainder = Decimal(business_miles - 10_000) * MILEAGE_RATE_AFTER_10K
    return _round_tax(first_10k + remainder)


def compute_tax(
    gross_income: Decimal,
    total_expenses: Decimal,
) -> TaxBreakdown:
    """Compute full tax breakdown for a sole trader in a given tax year."""
    net_profit = max(gross_income - total_expenses, Decimal("0"))

    personal_allowance = calculate_personal_allowance(net_profit)
    taxable_income = max(net_profit - personal_allowance, Decimal("0"))

    basic, higher, additional = calculate_income_tax(taxable_income)
    total_income_tax = basic + higher + additional

    class_2 = calculate_class_2_nic(net_profit)
    class_4 = calculate_class_4_nic(net_profit)
    total_nic = class_2 + class_4

    total_tax = total_income_tax + total_nic

    effective_rate = Decimal("0")
    if net_profit > 0:
        effective_rate = _round_tax((total_tax / net_profit) * 100)

    months_remaining = 12  # simplified — could be dynamic
    suggested_set_aside = (
        _round_tax(total_tax / months_remaining) if months_remaining > 0 else total_tax
    )

    return TaxBreakdown(
        gross_income=gross_income,
        total_expenses=total_expenses,
        net_profit=net_profit,
        personal_allowance=personal_allowance,
        taxable_income=taxable_income,
        basic_rate_tax=basic,
        higher_rate_tax=higher,
        additional_rate_tax=additional,
        total_income_tax=total_income_tax,
        class_2_nic=class_2,
        class_4_nic=class_4,
        total_nic=total_nic,
        total_tax_due=total_tax,
        effective_rate=effective_rate,
        approaching_vat_threshold=gross_income >= VAT_REGISTRATION_THRESHOLD * Decimal("0.8"),
        suggested_monthly_set_aside=suggested_set_aside,
    )
