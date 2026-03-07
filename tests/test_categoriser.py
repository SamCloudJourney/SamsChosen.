"""Tests for the transaction categorisation engine."""

from app.models.transaction import SA103Category, TransactionType
from app.services.categoriser import categorise_transaction


def test_income_detection():
    result = categorise_transaction("BACS CREDIT FROM CLIENT ABC", 1500.00)
    assert result.transaction_type == TransactionType.INCOME
    assert result.category == SA103Category.TURNOVER


def test_travel_expense():
    result = categorise_transaction("TFL OYSTER TOPUP", -20.00)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.TRAVEL


def test_office_software():
    result = categorise_transaction("GITHUB PRO SUBSCRIPTION", -4.00)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.OFFICE_COSTS


def test_advertising():
    result = categorise_transaction("GOOGLE ADS PAYMENT", -150.00)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.ADVERTISING


def test_bank_fees():
    result = categorise_transaction("MONTHLY BANK CHARGE", -5.50)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.FINANCIAL_CHARGES


def test_uncategorised_fallback():
    result = categorise_transaction("MYSTERIOUS PAYMENT XYZ123", -42.00)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.UNCATEGORISED
    assert result.confidence == 0.0


def test_office_rent():
    result = categorise_transaction("WEWORK MONTHLY RENT", -350.00)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.PREMISES


def test_phone_bill():
    result = categorise_transaction("VODAFONE MONTHLY BILL", -28.00)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.OFFICE_COSTS


def test_fuel():
    result = categorise_transaction("SHELL PETROL STATION", -45.00)
    assert result.transaction_type == TransactionType.EXPENSE
    assert result.category == SA103Category.TRAVEL


def test_positive_amount_not_expense():
    """Positive amounts should not match expense rules."""
    result = categorise_transaction("SHELL PETROL STATION", 45.00)
    assert result.transaction_type == TransactionType.INCOME
