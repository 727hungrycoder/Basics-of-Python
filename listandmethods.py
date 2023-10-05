l1 = [3, 5, 234, 234, 234, "harry", 9, 10, 12]
# contains same elements  and can also contains strings and numbers together
# list can be modified. Does not need to return a new list when modified
print(l1)
print(type(l1))   # will give the class list
l1.remove("harry")
print(l1)

# Methods in strings python.Strings are immutable but list can be changed.see the syntax differences in strings and list
# we directly print l1 in list whereas in string we cant directly print name.
name = "harrry"
print(name.upper())  # convert the words to capital letters
print(name.capitalize())   # convert the first letter of the word to capital letter
print(name.count("y"))    # GIVE THE COUNT OF occurences OF EACH LETTER
print(name.isalnum())    # GIVES True if the string is made up of alphanumeric characters

# count method in list will not return list but a number therefore its syntax is different
print(l1.count(234))  # give sthe count of item in the list

# when we want to modify the list we dont need to store it in another variable.Lisst are mutable that is can be modified.

l2=[1,4,7,32,87,5]
l2.sort()    # sorts the list in ascending order
l2.pop()   # removes the last element
print(l2.index(7))   # gives the index of the element of the array
print(l2)


# list can be changed and are mutable
l2[0] ='j'
print(l2)  # therefore lists can be changed


