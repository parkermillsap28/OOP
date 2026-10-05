class Faculty:
    def __init__(self):
        self.faculty_id = ""
        self.faculty_name = ""
        self.department = ""
        self.faculty_courses = ""
    def create_faculty(self):
        self.faculty_id = input("Enter faculty ID: ")
        self.faculty_name = input("Enter faculty name: ")
        self.department = input("Enter department: ")
        self.faculty_courses = input("Enter faculty courses: ")
    def enroll_student(self, student):
        self.faculty_id = student.id
        self.faculty_name = student.name


class Student:
    def __init__(self):
        self.student_id = ""
        self.student_name = ""
        self.major = ""
        self.student_courses = ""
        self.student_advisor = ""

    def create_new_student(self):
        self.student_id = input("Enter student ID: ")
        self.student_name = input("Enter student name: ")
        self.major = input("Enter student major: ")
        self.student_courses = input("Enter student courses: ")
    def display_student(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Major:", self.major)
        print("Courses:", self.student_courses)
    def assign_advisor(self):
        faculty_id = input("Enter faculty ID: ")
        if faculty_id in myFaculty:
            Stu.student_advisor(faculty_id)
            myStudents.append(Stu)
        else:
            print("Invalid faculty ID")

class Courses:
    def __init__(self):
        self.course_name = ""
    def create_course(self):
        Cou.course_name = input("Enter course name: ")
        Cou.assign_faculty(self.faculty_id)

myStudents = []
myFaculty = []
myCourses = []
Stu = Student()
Fac = Faculty()
Cou = Courses()
while 1:
    print("1. Student Settings")
    print("2. Faculty Settings")
    print("3. Course Settings")
    print("4. Display students")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        for :


        Stu.create_new_student()
        myStudents.append(Stu)
    elif choice == 2:
        Fac.create_faculty()
        myFaculty.append(Fac)
    elif choice == 3:
    elif choice == 4:
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")




