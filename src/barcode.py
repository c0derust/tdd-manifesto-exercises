"""
Kata 5: Point of sale kata
Create a simple app for scanning bar codes to sell products.

Requirements
1. Barcode '12345' should display price '$7.25'

2. Barcode '23456' should display price '$12.50'

3. Barcode '99999' should display 'Error: barcode not found'

4. Empty barcode should display 'Error: empty barcode'

5. Introduce a concept of total command where it is possible to scan multiple items. The command would display the sum of the scanned product prices
"""


def scan(barcode: str, price_db: dict) -> str:
    if barcode == "":
        return "Error: empty barcode"
    return price_db.get(barcode, "Error: barcode not found")


def total_scan(barcodes: list[str], price_db: dict) -> float:
    total = 0
    for code in barcodes:
        price = price_db.get(code, "$0")
        total += float(price[1:])

    return total
