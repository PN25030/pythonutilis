import json

def validate_mandatory_params(data):
    required_keys = [
        "gcp_project_id",
        "topic_name",
        "file_format",
        "IngestMethod",
        "is_pii_data_present",
        "action",
        "subaction"
    ]
    
    for key in required_keys:
        if key not in data:
            return False, f"Missing required key: {key}"
    
    return True, "Mandatory parameters are valid."

def validate_exceptional_params(data):
    # Add validation checks for exceptional cases here
    # For example, you can check specific values or formats
    
    return True, "Exceptional parameters are valid."

def validate_json(json_data):
    try:
        data = json.loads(json_data)
        if not isinstance(data, dict):
            return False, "JSON is not a dictionary."

        # Validate mandatory parameters
        is_mandatory_valid, mandatory_message = validate_mandatory_params(data)
        if not is_mandatory_valid:
            return False, mandatory_message
        
        subaction = data["subaction"]
        if not isinstance(subaction, dict):
            return False, "subaction is not a dictionary."

        # Validate exceptional parameters
        is_exceptional_valid, exceptional_message = validate_exceptional_params(data)
        if not is_exceptional_valid:
            return False, exceptional_message

        return True, "JSON is valid."
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON format: {str(e)}"

# Example JSON
json_data = """
{
    "gcp_project_id": "prj-d-digdataviz",
    "topic_name": "prjddigdataviz_dlu",
    "file_format": "parquet",
    "IngestMethod": "append",
    "is_pii_data_present": "Y/N",
    "action": "bqload",
    "subaction": {
        "dataset_id": "data",
        "table_name": "name",
        "pii_tags": "pii_col1:tag1, pii_col2:tag2"
    }
}
"""

# Validate the JSON
is_valid, message = validate_json(json_data)
print(message)


def read_properties_to_dict(file_path):
    try:
        data = {}
        with open(file_path, 'r') as properties_file:
            for line in properties_file:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    data[key.strip()] = value.strip()
        
        return data
    except FileNotFoundError:
        print("Properties file not found.")
        return {}

# Usage
properties_file_path = 'example.properties'
properties_data = read_properties_to_dict(properties_file_path)
print(properties_data)
