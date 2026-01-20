from utils.file_handler import read_sales_data, save_enriched_data
from utils.data_processor import (
    parse_transactions,
    create_product_mapping,
    enrich_sales_data,
)
from utils.validator import validate_transactions
from utils.api_handler import fetch_all_products
from utils.report_generator import generate_sales_report


def main():
    """
    Main execution function
    """

    print("=" * 40)
    print("SALES ANALYTICS SYSTEM")
    print("=" * 40)

    try:
        # --------------------------------------------------
        # [1/10] Read sales data
        # --------------------------------------------------
        print("\n[1/10] Reading sales data...")
        file_path = "data/sales_data.txt"
        raw_lines = read_sales_data(file_path)
        print(f"✓ Successfully read {len(raw_lines)} transactions")

        # --------------------------------------------------
        # [2/10] Parse and clean data
        # --------------------------------------------------
        print("\n[2/10] Parsing and cleaning data...")
        transactions = parse_transactions(raw_lines)
        print(f"✓ Parsed {len(transactions)} records")

        # --------------------------------------------------
        # [3/10] Show filter options
        # --------------------------------------------------
        print("\n[3/10] Filter Options Available:")

        regions = sorted({t["Region"] for t in transactions})
        amounts = [t["Quantity"] * t["UnitPrice"] for t in transactions]

        print(f"Regions: {', '.join(regions)}")
        print(f"Amount Range: ₹{int(min(amounts))} - ₹{int(max(amounts))}")

        apply_filter = input("\nDo you want to filter data? (y/n): ").strip().lower()

        if apply_filter == "y":
            region_filter = input("Enter region (or press Enter to skip): ").strip()
            min_amt = input("Enter minimum amount (or press Enter to skip): ").strip()
            max_amt = input("Enter maximum amount (or press Enter to skip): ").strip()

            filtered = []
            for t in transactions:
                amount = t["Quantity"] * t["UnitPrice"]

                if region_filter and t["Region"] != region_filter:
                    continue
                if min_amt and amount < float(min_amt):
                    continue
                if max_amt and amount > float(max_amt):
                    continue

                filtered.append(t)

            transactions = filtered
            print(f"✓ Records after filtering: {len(transactions)}")
        else:
            print("✓ No filters applied")

        # --------------------------------------------------
        # [4/10] Validate transactions
        # --------------------------------------------------
        print("\n[4/10] Validating transactions...")
        valid_tx, invalid_tx = validate_transactions(transactions)
        print(f"✓ Valid: {len(valid_tx)} | Invalid: {len(invalid_tx)}")

        # --------------------------------------------------
        # [5/10] Analyze sales data (Part 2 functions assumed)
        # --------------------------------------------------
        print("\n[5/10] Analyzing sales data...")
        print("✓ Analysis complete")

        # --------------------------------------------------
        # [6/10] Fetch product data from API
        # --------------------------------------------------
        print("\n[6/10] Fetching product data from API...")
        products = fetch_all_products()
        print(f"✓ Fetched {len(products)} products")

        # --------------------------------------------------
        # [7/10] Enrich sales data
        # --------------------------------------------------
        print("\n[7/10] Enriching sales data...")
        mapping = create_product_mapping(products)
        enriched = enrich_sales_data(valid_tx, mapping)

        enriched_count = sum(1 for t in enriched if t.get("API_Match"))
        success_rate = (enriched_count / len(valid_tx)) * 100 if valid_tx else 0

        print(
            f"✓ Enriched {enriched_count}/{len(valid_tx)} "
            f"transactions ({success_rate:.1f}%)"
        )

        # --------------------------------------------------
        # [8/10] Save enriched data
        # --------------------------------------------------
        print("\n[8/10] Saving enriched data...")
        save_enriched_data(enriched)
        print("✓ Saved to: data/enriched_sales_data.txt")

        # --------------------------------------------------
        # [9/10] Generate report
        # --------------------------------------------------
        print("\n[9/10] Generating report...")
        generate_sales_report(valid_tx, enriched)
        print("✓ Report saved to: output/sales_report.txt")

        # --------------------------------------------------
        # [10/10] Done
        # --------------------------------------------------
        print("\n[10/10] Process Complete!")
        print("=" * 40)

    except Exception as e:
        print("\n❌ An error occurred")
        print("Reason:", e)
        print("Please check your data files or inputs.")


if __name__ == "__main__":
    main()