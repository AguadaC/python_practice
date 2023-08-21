# Overview

The provided script is a command-line tool designed to quickly visualize the contents of JSON and CSV files in a human-readable format. It allows users to view the data stored in these files without the need for specialized software. The script determines the file type based on the provided filename's extension and then displays the content accordingly.

# How to Use
## Requirements:

- Python: The script is written in Python and requires Python to be installed on your system.
- `tabulate` Library: To display CSV data, the script uses the tabulate library. You need to install this library before using the script. You can install it using the following command:
    - `pip install tabulate`

## Download the Script:

- Download the script and save it as a .py file, e.g., file_viewer.py.

## Command-line Usage:

- Open a terminal or command prompt.
- Navigate to the directory where you saved the script and the file you want to visualize.

## View JSON Files:

- To view the contents of a JSON file, use the following command:
    - `python file_viewer.py file.json`
- Replace file.json with the actual name of your JSON file.

## View CSV Files:

- To view the contents of a CSV file, use the following command:
    - `python file_viewer.py file.csv`
- Replace file.csv with the actual name of your CSV file.

## Output:

- The script will output the content of the specified file in a readable format.
- For JSON files, it will pretty-print the JSON data with an indentation of 4 spaces.
- For CSV files, it will display the data in a tabular format using the tabulate library.

## Error Handling:

- If the specified file is not found, the script will inform you.
- If the file's content is not valid JSON (for JSON files) or the file type is not recognized, the script will raise an appropriate error.

## Note:

- Make sure you provide the correct file extension (json or csv) in the command.
- The script assumes that the CSV file has headers in the first row. It uses these headers for column names when displaying the table.