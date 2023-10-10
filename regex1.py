import re

test_string = "hello _123"


pattern = re.compile(r'[lo]')          # this is called set
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

pattern = re.compile(r'\w')                   # matches for any alphanumeric character
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

pattern = re.compile(r'[a-z]')                   # matches for any alphanumeric character
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

pattern = re.compile(r'[1-9]')                   # matches for any digit
matches = pattern.finditer(test_string)

for match in matches:
    print(match)


pattern = re.compile(r'[1-9a-zA-Z]')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

pattern = re.compile(r'\d')                   # matches for any decimal
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

