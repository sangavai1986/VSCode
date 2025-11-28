def validate_json_key(json_data, key,expected_value):
    if key not in json_data:
        return False, f"Key '{key}' not found in JSON."

    actual_value = json_data.get(key)

    # If value is a list → membership check
    if isinstance(actual_value, list):
        if expected_value not in actual_value:
            return False, (
                f"Value '{expected_value}' not found in list for key '{key}'. "
                f"Actual list: {actual_value}"
            )
        print(f"PASS: '{expected_value}' found in '{key}'")   # <-- PASS MESSAGE
        return True, None

    # Regular equality check
    if actual_value != expected_value:
        return False, (
            f"Value mismatch for key '{key}'. "
            f"Expected: {expected_value}, Got: {actual_value}"
        )

    print(f"PASS: {key} == {expected_value}")      # <-- PASS MESSAGE
    return True, None

def validate_json_value(structure, expected_value):
    if structure != expected_value:
        return 0,f"Value mismatch for '{structure}': Expected {expected_value}"
        
    return 1, None
