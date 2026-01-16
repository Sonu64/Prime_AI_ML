class Person:
    def __init__(self, name, age=20, address="Default Address"):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"

# Only name
p1 = Person("Sonu")
print(p1)

# name + age
p2 = Person("Shanu", 22)
print(p2)

# name + age + address
p3 = Person("Suparna", 19, "Panchbaga")
print(p3)