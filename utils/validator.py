def validate_transactions(transactions):
    valid = []
    invalid = []

    for tx in transactions:
        if (
            not tx["CustomerID"]
            or not tx["Region"]
            or tx["Quantity"] <= 0
            or tx["UnitPrice"] <= 0
            or not tx["TransactionID"].startswith("T")
        ):
            invalid.append(tx)
        else:
            valid.append(tx)

    return valid, invalid

