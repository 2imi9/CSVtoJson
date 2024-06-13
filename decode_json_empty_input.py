import json

# Define the file paths
input_json_file_path = r"C:\Users\frank\Desktop\csv_to_json\json.json"
output_json_file_path = r"C:\Users\frank\Desktop\csv_to_json\decoded_json_empty_input.json"

# Function to decode Unicode escape sequences
def decode_unicode_escape(s):
    try:
        # Decode as UTF-8 directly
        return s.encode('latin1').decode('utf-8')
    except UnicodeEncodeError:
        # If that fails, return the original string
        return s

# Read the JSON file
with open(input_json_file_path, "r", encoding='utf-8') as f:
    data = json.load(f)

# Process the JSON data
for entry in data["qa_data"]:
    entry["instruction"] = decode_unicode_escape(entry["instruction"])
    entry["output"] = decode_unicode_escape(entry["output"])
    # Set the "input" section to an empty string
    entry["input"] = ""

# Write the modified data to a new JSON file
with open(output_json_file_path, "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Conversion complete. Modified JSON written to", output_json_file_path)
