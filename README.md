# Codebase Knowledge Extractor

## Description

This is a small program that takes in code from a Python Weather Info App, and extracts and organizes function data from it. The final output is a structured JSON file containing function names, descriptions, parameters, file names, and manually assigned purpose categories.

## How to Run

1. Activate the environment: 
`source venv/bin/activate` 
2. Run `pip install -r requirements.txt`
3. Run the script: `python3 extract.py` 
4. Open data.ipynb in VS Code/Jupyter and run all cells

## Data Dictionary

- `function_name`: Name of the function extracted from the Python file
- `description`: Comment or explanation associated with the function
- `parameters`: Inputs accepted by the function
- `file_name`: Source file where the function appears
- `purpose`: Manually assigned category describing the function’s role

## Outputs

- `extracted_functions.csv`: raw extracted function data from the source code
- `weather_app_functions.json`: cleaned and structured function metadata

## Tools Used
- Python 3.9+
- Pandas
- OS Library  
- VS Code / Jupyter Notebook

## Lessons Learned
- Data extraction
- AST parsing
- DataFrame to JSON creation
- Data cleaning