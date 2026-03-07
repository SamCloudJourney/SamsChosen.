"""Tests for the UK tax calculation engine."""

from decimal import Decimal

from app.services.tax_calculator import (
    calculate_class_2_nic,
    calculate_class_4_nic,
    calculate_home_office_deduction,
    calculate_income_tax,
    calculate_mileage_deduction,
    calculate_personal_allowance,
    compute_tax,
)


def test_personal_allowance_standard():
    assert calculate_personal_allowance(Decimal("50000")) == Decimal("12570")


def test_personal_allowance_tapers():
    # £110,000 income -> £100k taper starts, lose £1 per £2 above £100k
    # £10,000 above threshold -> lose £5,000
    result = calculate_personal_allowance(Decimal("110000"))
    assert result == Decimal("7570")


def test_personal_allowance_fully_tapered():
    # Above £125,140 -> £0 allowance
    result = calculate_personal_allowance(Decimal("150000"))
    assert result == Decimal("0")


def test_income_tax_basic_only():
    # £20,000 taxable income -> all at 20%
    basic, higher, additional = calculate_income_tax(Decimal("20000"))
    assert basic == Decimal("4000.00")
    assert higher == Decimal("0")
    assert additional == Decimal("0")


def test_income_tax_into_higher():
    # £50,000 taxable income -> £37,700 at 20% + £12,300 at 40%
    basic, higher, additional = calculate_income_tax(Decimal("50000"))
    assert basic == Decimal("7540.00")
    assert higher == Decimal("4920.00")
    assert additional == Decimal("0")


def test_class_2_nic_below_threshold():
    assert calculate_class_2_nic(Decimal("5000")) == Decimal("0")


def test_class_2_nic_above_threshold():
    result = calculate_class_2_nic(Decimal("30000"))
    assert result == Decimal("179.40")


def test_class_4_nic_below_lower():
    assert calculate_class_4_nic(Decimal("10000")) == Decimal("0")


def test_class_4_nic_in_main_band():
    # Profits £30,000 -> (30000 - 12570) * 6% = 17430 * 0.06 = 1045.80
    result = calculate_class_4_nic(Decimal("30000"))
    assert result == Decimal("1045.80")


def test_class_4_nic_above_upper():
    # Profits £60,000 -> main band (50270-12570)*6% + (60000-50270)*2%
    result = calculate_class_4_nic(Decimal("60000"))
    main = (Decimal("50270") - Decimal("12570")) * Decimal("0.06")
    extra = (Decimal("60000") - Decimal("50270")) * Decimal("0.02")
    expected = (main + extra).quantize(Decimal("0.01"))
    assert result == expected


def test_home_office_high_hours():
    assert calculate_home_office_deduction(120) == Decimal("26") * 12


def test_home_office_medium_hours():
    assert calculate_home_office_deduction(60) == Decimal("18") * 12


def test_home_office_low_hours():
    assert calculate_home_office_deduction(30) == Decimal("10") * 12


def test_home_office_too_few_hours():
    assert calculate_home_office_deduction(10) == Decimal("0")


def test_mileage_under_10k():
    result = calculate_mileage_deduction(5000)
    assert result == Decimal("2250.00")


def test_mileage_over_10k():
    result = calculate_mileage_deduction(15000)
    expected = Decimal("10000") * Decimal("0.45") + Decimal("5000") * Decimal("0.25")
    assert result == expected.quantize(Decimal("0.01"))


def test_compute_tax_full():
    """Integration test: full tax computation for a £45k freelancer with £5k expenses."""
    result = compute_tax(Decimal("45000"), Decimal("5000"))
    assert result.net_profit == Decimal("40000")
    assert result.personal_allowance == Decimal("12570")
    assert result.taxable_income == Decimal("27430")
    assert result.total_income_tax > Decimal("0")
    assert result.total_nic > Decimal("0")
    assert result.total_tax_due == result.total_income_tax + result.total_nic
    assert not result.approaching_vat_threshold


def test_compute_tax_vat_warning():
    """Should flag approaching VAT threshold when income >= 80% of £90k."""
    result = compute_tax(Decimal("75000"), Decimal("2000"))
    assert result.approaching_vat_threshold


def test_compute_tax_zero_income():
    result = compute_tax(Decimal("0"), Decimal("0"))
    assert result.total_tax_due == Decimal("0")
    assert result.effective_rate == Decimal("0")
