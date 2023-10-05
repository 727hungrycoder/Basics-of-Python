name = "Harry"
print(name)

number="7"

print(name[0:3])  # print the name between 0 and 2
print(name[1:4])  # print the name between 1 and 3
# print(name[a:b])  # print between a and b-1
print(name[1:4])

# Methods in strings python

print(name.upper())  # convert the words to capital letters
print(name.capitalize())   # convert the first letter of the word to capital letter
print(name.count("y"))    # GIVE THE COUNT OF occurences OF EACH LETTER
print(name.isalnum())    # GIVES True if the string is made up of alphanumeric characters

print(number.isnumeric())  # if the string is a number gives true
print(name.isnumeric())    # if the string is not a number gives false

# Multiline strings

a1 = '''harry 
is  a good boy'''
a2 = 'harry is  a good boysss'
a3 = "harry is  a good boys"
print(a1, a2, a3)

# strings cannot be changed and are immutable
# a1[0] ='j' will give an error
