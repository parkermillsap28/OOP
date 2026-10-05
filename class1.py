class Student:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""

    def create_new_student(self):
        self.id = input("Enter student ID: ")
        self.name = input("Enter student name: ")
        self.department = input("Enter student department: ")
    def display_student(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
myStudents = []
Stu = Student()
while 1:
    print("1. Create new student")
    print("2. Display students")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Stu.create_new_student()
        myStudents.append(Stu)
    elif choice == 2:
        Stu.display_student()
    elif choice == 3:
        exit()
    else:
        print("Invalid choice")


class Faculty:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.department = ""

