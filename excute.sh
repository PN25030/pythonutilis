#!/bin/bash

# Run the Python script and capture the output
result=$(python validate_json.py)

# Extract the validation result and message from the output
is_valid=$(echo "$result" | awk '{print $1}')
message=$(echo "$result" | cut -d ' ' -f 2-)

# Use the validation result and message in your bash script logic
if [ "$is_valid" == "True" ]; then
    echo "Validation successful: $message"
else
    echo "Validation failed: $message"
fi
