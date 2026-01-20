import os
from datetime import datetime

def generate_sales_report(transactions, products, output_file="output/sales_report.txt"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    total_revenue = sum(tx["Quantity"] * tx["UnitPrice"] for tx in transactions)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 40 + "\n")
        f.write("SALES ANALYTICS REPORT\n")
        f.write("=" * 40 + "\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"Valid Transactions: {len(transactions)}\n")
        f.write(f"Total Revenue: ₹{total_revenue:.2f}\n")
