# We cannot give in space in variable names
# it can be started with underscore and cannot be started with special characters
from _ast import Not  # importing Not operator

num1 = 10
_num2 = 34
num2 = 2

# arithmatic operators

# press alt for multiple cursors
print("num1 + num2 is", num1 + num2)
print("num1 - num2 is", num1 - num2)
print("num1 * num2 is", num1 * num2)
print("num1 / num2 is", num1 / num2)
print("num1 // num2 is", num1 // num2)  # removes the numbers after decimals
print("num1 % num2 is", num1 % num2)    #gives the remainder
print("num1 ** num2 is", num1 ** num2)  #gives the power

# Assinment operators

a = 4
a += 4
print(a)
a -= 4
print(a)
a *= 4
a /= 4
print(a)
#  a //= 4  will give an error
#a %= 4  will give an error
#a **= 4  will give an error


# COMPARISION OPERATORS
x=5
y=10
z=2
print(x > y)
print(x > y)
print(x != y)
print(x == y)

'''
output will be a boolean of comparision operator
False
False
True
False
'''

# Logical operators and or not operator

print(x == z and x > y)
print(x == z or x > y)
print(not True)  #not operator should be smaller case
print(not False)








