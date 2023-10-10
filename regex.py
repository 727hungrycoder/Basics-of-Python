import re  # Regular expressions inside Python are made available through the `re module.
test_string = '123abc456789abc123ABC.ABC'
pattern = re.compile(r'abc')
matches = pattern.finditer(test_string)

for match in matches:
    print(match)
    print(match.span(), match.start(), match.end())
    print(match.group())  # returns the string


# https://www.youtube.com/watch?v=AEE9ecgLgdQ

#above is youtube link to study regex

## Use raw strings for the search pattern
a = '\tHello'
b = r'\tHello'  # we use smallcase r to input the raw string
print(a)
print(b)


my_string = 'abc123ABC123abc.ABC'
# findall()  Find all substrings where the RE matches, and returns them as a list.
pattern = re.compile(r'123')
matches = pattern.findall(my_string)
for match in matches:
    print(match)

# match  will match only if the string is at beginning otherwise it will print none.

pattern = re.compile(r'123')
match = pattern.match(my_string)
print(match)


# search(): Scan through a string, looking for any location where this RE matches.
pattern = re.compile(r'123')
match = pattern.search(my_string)
print(match)



# Methods used in matches

pattern  = re.compile((r"123"))
matches = pattern.finditer(test_string)

for match in matches:
    print(match.span(),match.start(),match.end(),match.group())

# Dot character
pattern  = re.compile((r"."))
matches = pattern.finditer(test_string)

for match in matches:
    print(match)


pattern  = re.compile((r"\."))
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

pattern  = re.compile((r"^123"))
matches = pattern.finditer(test_string)

for match in matches:
    print(match)


pattern  = re.compile((r"ABC$"))
matches = pattern.finditer(test_string)

for match in matches:
    print(match)


pattern  = re.compile((r"ABC$"))
matches = pattern.finditer(test_string)

for match in matches:
    print(match)

