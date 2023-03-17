class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printName(self):
        print(f"Name: {self.name} & Alter: {self.age}" )

person = Person("Hans", 59)
person.printName()
# test