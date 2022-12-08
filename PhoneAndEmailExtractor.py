#!python3

#phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip,re

phoneRegex = re.compile('''(
    (\d{2,3}|\(\d{2,3}\))?  # area code
    (\s)?                   # separator
    (\d{4,5})               # first 5 to 4 digits
    (-)?                    # separator
    (\d{4})                 # last 4 digits
)''', re.VERBOSE)

# TODO: Create email regex.
# TODO: Find matches in clipboard text.
# TODO: Copy results to the clipboard.

# Create email regex.

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @                   # @ symbol
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
)''', re.VERBOSE)

# TODO: Find matches in clipboard text.


# Find matches in the clipboard text.

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    # if groups[8] != '':
    #     phoneNum = 'x' + groups[8]
    #     matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard.

# Copy results to clipboard

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to the clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses were found.')