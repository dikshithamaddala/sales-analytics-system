def parse_transactions(raw_lines):
    """
    Parses raw lines into clean transaction dictionaries
    """
    transactions = []

    for line in raw_lines:
        line = line.strip()
        if not line:
            continue

        parts = line.split("|")
        if len(parts) != 8:
            continue

        try:
            transaction_id, date, product_id, product_name, quantity, unit_price, customer_id, region = parts

            product_name = product_name.replace(",", "").strip()
            quantity = int(quantity.replace(",", ""))
            unit_price = float(unit_price.replace(",", ""))

            transaction = {
                "TransactionID": transaction_id.strip(),
                "Date": date.strip(),
                "ProductID": product_id.strip(),
                "ProductName": product_name,
                "Quantity": quantity,
                "UnitPrice": unit_price,
                "CustomerID": customer_id.strip(),
                "Region": region.strip()
            }

            transactions.append(transaction)

        except ValueError:
            continue

    return transactions


def create_product_mapping(products):
    mapping = {}
    for product in products:
        mapping[str(product["id"])] = product
    return mapping


def enrich_sales_data(transactions, product_mapping):
    enriched = []

    for tx in transactions:
        product = product_mapping.get(tx["ProductID"])

        if product:
            tx["API_Match"] = True
            tx["Category"] = product.get("category", "Unknown")
        else:
            tx["API_Match"] = False
            tx["Category"] = "Unknown"

        enriched.append(tx)

    return enriched

