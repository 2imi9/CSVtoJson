import json

# Define the file paths
input_json_file_path = r"C:\Users\frank\Desktop\csv_to_json\json.json"
output_json_file_path = r"C:\Users\frank\Desktop\csv_to_json\decoded_json.json"

# Function to decode Unicode escape sequences
def decode_unicode_escape(s):
    try:
        # First, try to decode as utf-8 directly
        return s.encode('latin1').decode('utf-8')
    except UnicodeEncodeError:
        # If that fails, return the original string
        return s

# Read the JSON file
with open(input_json_file_path, "r", encoding='utf-8') as f:
    data = json.load(f)

# Decode the improperly encoded utf-8 sequences in the JSON data
for entry in data["qa_data"]:
    entry["instruction"] = decode_unicode_escape(entry["instruction"])
    entry["input"] = decode_unicode_escape(entry["input"])
    entry["output"] = decode_unicode_escape(entry["output"])

# Write the decoded data to a new JSON file
with open(output_json_file_path, "w", encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("Conversion complete. Decoded JSON written to", output_json_file_path)
