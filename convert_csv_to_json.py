import csv
import json

# Define the file paths
csv_file_path = r"C:\Users\frank\Desktop\csv_to_json\csv.csv"
json_file_path = r"C:\Users\frank\Desktop\csv_to_json\json.json"

# Open the CSV file for reading with utf-8 encoding
with open(csv_file_path, "r", encoding='utf-8') as f:
    csvReader = csv.reader(f)
    # Skip the header row if there is one
    next(csvReader)

    # Initialize the dictionary to hold JSON data
    qa_data = {"qa_data": []}

    # Iterate over the rows in the CSV reader object
    for row in csvReader:
        # Append the data from each row to the dictionary
        qa_data["qa_data"].append({
            "instruction": row[0],
            "input": row[0],
            "output": row[1]
        })

# Open the JSON file for writing
with open(json_file_path, "w", encoding='utf-8') as f:
    # Dump the dictionary into the JSON file with indentation for readability
    json.dump(qa_data, f, indent=4)
