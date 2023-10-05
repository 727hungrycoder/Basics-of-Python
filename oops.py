class Employee:                             #use class to define an object
    def __init__(self, name, salary):       #us constructor for name and salary and use __init__
        self.name = name
        self.salary = salary

    def get_salary(self):                  #define methoda
        print(self.salary)


# create object using classes as below

harry = Employee("Harry","670000000")
print(harry.salary)
print(harry.name)
harry.get_salary()
