# Sales Analytics System

A Python-based Sales Analytics application that reads raw sales data from a text file, cleans and validates it, enriches it using an external API, and generates a comprehensive analytics report.


## Project Structure
sales_analytics/
│
├── data/
│ ├── sales_data.txt
│ └── enriched_sales_data.txt
│
├── output/
│ └── sales_report.txt
│
├── utils/
│ ├── init.py
│ ├── file_handler.py
│ ├── data_processor.py
│ ├── validator.py
│ ├── api_handler.py
│ └── report_generator.py
│
├── main.py
└── README.md


## Requirements
- Python 3.10 or higher
- `requests` library


## Setup Instructions
1. Open the project folder in VS Code
2. Open terminal in VS Code
3. Install dependencies:
   ```bash
   python3 -m pip install requests


## Data File
The sales data file is provided and must be placed at:
data/sales_data.txt


## How to Run
Run the application from the project root:
python3 main.py


## Console Output
The program prints step-by-step progress including:
Total records parsed
Invalid records removed
Valid records after cleaning
API fetch status
Enrichment success rate
Output file locations


## Output Files
Enriched data:
data/enriched_sales_data.txt

Final report:
output/sales_report.txt


## Features Implemented
Encoding-safe file reading
Data parsing and cleaning
Transaction validation
Optional user filtering
Sales analysis
API-based enrichment
Report generation
Error handling