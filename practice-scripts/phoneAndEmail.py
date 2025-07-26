import pyperclip, re
# Find and copy email and phone numbers from clipboard

# Regex for finding phone numbers
phone_re = re.compile(r'''(
(\d{3}|\(\d{3}\))? # Area code
(s]|-|\.)? # Seperator
(\d{3}) # First 3 digits
(\s|-|\.) # Seperator
(\d{4}) # Last 4 digits
(s*(ext|x|ext\.)\s*(\d{2,5}))? # Extenstion
)''', re.VERBOSE)

# Regex for finding emails
email_re = re.compile(r'''(
[a-xA-Z0-9._%+-]+ # username
@ # @ symbol
[a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dont-something
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phone_re.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[6] != '':
        phone_re += ' x' + groups[6]
    matches.append(phone_num)
for groups in email_re.findall(text):
    matches.append(groups[0])

# Copy the results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')