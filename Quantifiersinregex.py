"""Quantifier¶
* : 0 or more
+ : 1 or more
? : 0 or 1, used when a character can be optional
{4} : exact number
{4,6} : range numbers (min, max)"""



import re

test_string = "hello_world123"

pattern = re.compile(r'123*')

matches = pattern.finditer(test_string)

for match in matches:
    print(match)


pattern = re.compile(r'1*')

matches = pattern.finditer(test_string)

for match in matches:
    print(match)

test_string1 = "hello_world_1_2_3_"

pattern = re.compile(r'_1?')

matches = pattern.finditer(test_string1)

for match in matches:
    print(match)

test_string1 = "hello_world_1_2_3_"

pattern = re.compile(r'_1+')

matches = pattern.finditer(test_string1)

for match in matches:
    print(match)

pattern = re.compile(r'\d{1,3}')

matches = pattern.finditer(test_string1)

for match in matches:
    print(match)



dates = """

hello
2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04

"""

pattern = re.compile(r'\d\d\d\d.\d\d.\d\d')

matches = pattern.finditer(dates)

for match in matches:
    print(match)


pattern = re.compile(r'\d\d\d\d[_/]\d\d[_/]\d\d')

matches = pattern.finditer(dates)

for match in matches:
    print(match)


pattern = re.compile(r'\d{4}[_/]\d{2}[_/]\d{2}')

matches = pattern.finditer(dates)

for match in matches:
    print(match)

my_string = """
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
"""


pattern = re.compile(r'Mr\s\w+')

matches = pattern.finditer(my_string)

for match in matches:
    print(match)

pattern = re.compile(r'Mr.\s\w+')

matches = pattern.finditer(my_string)

for match in matches:
    print(match)

pattern = re.compile(r'(Mr|Mrs|Ms)\.?\s\w+')

matches = pattern.finditer(my_string)

for match in matches:
    print(match)

# square brackets denotes set and round brackets denotes groups

emails = """
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""

pattern = re.compile(r'([A-Za-z0-9-]+)@([a-zA-Z-]+)\.([a-z]+)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)
    print(match.group(2))


pattern = re.compile(r'[\w\d-]+@[\w-]+\.[\w]+')

matches = pattern.finditer(emails)

for match in matches:
    print(match)


my_string = 'abc123ABCDEF123abc'

pattern = re.compile(r'123')

matches = pattern.split(my_string)

for match in matches:
    print(match)



for match in matches:
    print(match)

my_string = "hello world, you are the best world"
pattern = re.compile(r'world')
subbed_string = pattern.sub(r'planet', my_string)
print(subbed_string)


urls = """
http://python-engineer.com
https://www.python-engineer.org
http://www.pyeng.net
"""
pattern = re.compile(r'[\w]+://[\w\.]+[\w]')
matches = pattern.finditer(urls)

for match in matches:
    print(match)


pattern = re.compile(r'https?://(www\.)?([a-zA-Z-]+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match)
