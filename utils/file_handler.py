import os

def read_sales_data(file_path):
    """
    Reads raw sales data safely with encoding handling
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.readlines()
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="latin-1") as f:
            return f.readlines()


def save_enriched_data(enriched_data, output_path="data/enriched_sales_data.txt"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for tx in enriched_data:
            f.write(str(tx) + "\n")

