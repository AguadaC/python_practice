import csv
import json
import sys
from tabulate import tabulate

def print_file_content(filename):
    """
    Read and print the contents of a JSON or CSV file in a human-readable format.

    Parameters:
        filename (str): The name of the JSON or CSV file to read and print.

    Raises:
        FileNotFoundError: If the specified file is not found.
        ValueError: If the file type is not recognized (not JSON or CSV).
    """
    if filename.lower().endswith('.json'):
        try:
            with open(filename, 'r') as file:
                content = json.load(file)
                print(json.dumps(content, indent=4))
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
        except json.JSONDecodeError:
            print(f"The file '{filename}' is not valid JSON.")
    elif filename.lower().endswith('.csv'):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                table = [row for row in reader]
                print(tabulate(table, headers="firstrow", tablefmt="grid"))
        except FileNotFoundError:
            print(f"The file '{filename}' was not found.")
    else:
        raise ValueError(f"Unrecognized file type: '{filename}' is neither JSON nor CSV.")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        print_file_content(filename)
    else:
        print("Usage: python json_view.py file.json/csv")

