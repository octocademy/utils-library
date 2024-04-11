import re

# Regular expression for validating email addresses
email_regex = r'^[\w\.\+\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$'

# Regular expression for validating phone numbers
phone_regex = r'^(\+)?1?\d{9,15}$'

# Regular expression for validating secure URLs
secure_url_regex = r'^https:\/\/'

# Regular expression for validating GitHub URLs
github_url_regex = r'^https:\/\/github\.com\/[a-zA-Z0-9\-]+\/[a-zA-Z0-9\-]+'

def is_email_valid(email):
    """Check if the email matches the email regular expression."""
    return bool(re.search(email_regex, email))

def is_phone_valid(phone):
    """Check if the phone number matches the phone regular expression."""
    return bool(re.search(phone_regex, phone))

def is_secure_url_valid(url):
    """Check if the URL is a secure URL."""
    return bool(re.search(secure_url_regex, url))

def is_github_url_valid(url):
    """Check if the URL is a valid GitHub repository or subdomain URL."""
    return bool(re.search(github_url_regex, url))

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

    if is_secure_url_valid('https://example.com'):
        print("valid")
    else:
        print("invalid")

    if is_github_url_valid('https://github.com/octocademy/utils-library'):
        print("valid")
    else:
        print("invalid")
