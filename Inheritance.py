
class Person:
    def __init__(self, name, age, id, interests):
        self.name = name
        self.age = age
        self.id = id
        self.interests = interests
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.id)
        print("Interests:", self.interests)

class Student(Person):
    def __init__(self, a, b, c, d, x, y, z):
        Person.__init__(self, a, b, c, d)
        self.major = x
        self.gpa = y
        self.minor = z
    def display(self):
        Person.display(self)
        print(self.major)
        print(self.gpa)
        print(self.minor)


s1 = Student("Joe", "19", "1", "music", "CS", 3.9, "Cyb")
s1.display()