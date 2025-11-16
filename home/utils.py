import re

def is_valid_phone_number(phone_number: str) -> bool:
    """
    Validates a phone number using a regular expression.
    
    Accepts:
    - 10–12 digits
    - Optional spaces or hyphens
    - Optional country code like +1, +91, etc.
    
    Returns True if valid, False otherwise.
    """

    pattern = r'^\+?\d[\d\s\-]{9,14}\d$'
    # Explanation:
    # ^           - start of string
    # \+?         - optional +
    # \d          - first digit
    # [\d\s\-]{9,14} - allow digits, spaces, or hyphens for the next 9–14 characters
    # \d$         - end with a digit

    return bool(re.match(pattern, phone_number))