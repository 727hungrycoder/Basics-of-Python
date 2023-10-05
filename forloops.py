for i in range(5):
    print(i)

# i will print number from 0 to 4

a = [1, 34, 45, 78]
for item in a:
    print(item)
# similarly for the sets and tuples we use for loop

s = {34, 67, 67, 68}  # set will print only unique values as well as does not maintain orders.
print(s)
for item in s:
    print(item)

t = (34, 67, 67, 68)  # tuple  will print all  values with duplicates
print(t)
for item in t:
    print(item)

for i in range(5):
    if i==2:
        continue   # it will skip 2
    print(i)