import re

# Regular expression for validating email addresses
email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'

# Regular expression for validating phone numbers
phone_regex = r'^(\+)?1?\d{9,15}$'

def is_email_valid(email):
    """Check if the email matches the email regular expression."""
    return bool(re.search(email_regex, email))

def is_phone_valid(phone):
    """Check if the phone number matches the phone regular expression."""
    return bool(re.search(phone_regex, phone))

# Test all the regular expressions
if __name__ == '__main__':
    if is_email_valid('test@github.com'):
        print("valid")
    else:
        print("invalid")

    if is_phone_valid('4255552368'):
        print("valid")
    else:
        print("invalid")