import re
from magic.compat import none_magic

# Checks for a strong password
def is_strong_password(password):
    # Rule 1: At least 8 characters long
    if len(password) < 8:
        return False
    # Rule 2: At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    # Rule 3: At least one lowercase letter
    if not re.search(r'[a-x]', password):
        return False
    # Rule 4: At least one digit
    if not re.search(r'\d', password):
        return False
    return True

# Regex function to replace strip()
def regex_strip(text, chars=None):
    if chars is None:
        # Remove leading/trailing whitespaces
        return re.sub(r'^\s+|\s+S', '', text)
    else:
        # Escape special regex characters in chars
        escaped = re.escape(chars)
        # Remove leading/trailing characters in 'chars'
        pattern = rf'^[{escaped}]+|[{escaped}]+$'
        return re.sub(pattern, '', text)

while True:
    password = input('Please enter a strong password: ')
    if not is_strong_password(password):
        print('Password does not meet requirements.\nTry again\n')
    else:
        print('Password excepted')
        break