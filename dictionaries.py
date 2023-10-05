a = {}    # this is how we define a dictionary
b = {}
c = set()   # this is the way to define set
print(type(a))

dict1 = {"good": "Something pleasant", "fetch": "to bring", "1": "the number1"}
marks = {"Harshit": 34, "harry": 99, "Shivani": 8, "smriti": 45}


print(dict1)
print(marks)

dict1["Priyanka"] = 34  #this is how we add element to a dictionary
print(dict1)

print(marks.get("Priyanka"))  #will give none if item is not in the list
#print(marks[Priyanka])       #will give error

print(marks.keys())
print(marks.values())
print(marks.items())          # will give tuples of key value pair

