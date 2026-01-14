import pytest

from src.barcode import scan, total_scan


@pytest.fixture
def test_price_db():
    return {
        "12345": "$7.25",
        "23456": "$12.50",
    }


@pytest.mark.parametrize(
    ("code", "price"),
    [
        ("12345", "$7.25"),
        ("23456", "$12.50"),
    ],
)
def test_scan_displays_price(code, price, test_price_db):
    result = scan(code, test_price_db)

    assert result == price


def test_missing_barcode_error_message(test_price_db):
    result = scan("99999", test_price_db)

    assert result == "Error: barcode not found"


def test_empty_barcode_error_message(test_price_db):
    result = scan("", test_price_db)

    assert result == "Error: empty barcode"


def test_total_scan_sums_prices(test_price_db):
    result = total_scan(["12345", "23456"], test_price_db)

    assert result == 19.75
