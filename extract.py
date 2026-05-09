import os
import pandas as pd
import ast

file_path = "./Python-Weather-Info-App/weather_app.py"
data_list = [] # to store all the extracted functions

def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    lines_split = content.splitlines() # Split the content into lines for easier access to comments
    tree = ast.parse(content) # Parse the content of the file into an Abstract Syntax Tree (AST) to analyze its structure

    for node in ast.walk(tree):
        
        description = "No description provided" # Default description if no comment is found
        
        if isinstance(node, ast.FunctionDef): # Check if the node is a function definition
            comment_line = lines_split[node.lineno - 2] # Get the line just before the function definition to check for a comment
            if comment_line.strip().startswith("#"):
                description = comment_line.strip() # If the line is a comment, use it as the description for the function
        
        if isinstance(node, ast.FunctionDef):
            file_info = {
                "function_name": node.name,
                "description": description,
                "parameters": [arg.arg for arg in node.args.args],
            }

            data_list.append(file_info)

new_data = extract_data(file_path)

df = pd.DataFrame(data_list)

df.to_csv("extracted_functions.csv", index=False) #to save the extracted data to a CSV file

print("ETL complete! Your dataset is ready to view!")