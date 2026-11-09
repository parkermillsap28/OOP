import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Lab5DB"
)
mycursor = mydb.cursor()
mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS Student (
                    StudentID INT PRIMARY KEY,
                    Name VARCHAR(50),
                    Department VARCHAR(50),
                    Major VARCHAR(50),
                    Courses VARCHAR(50),
                    GPA VARCHAR(50)
                    )
                """)
mycursor.execute("""
                    CREATE TABLE IF NOT EXISTS Faculty (
                    FacultyID INT PRIMARY KEY,
                    Name VARCHAR(50),
                    Department VARCHAR(50),
                    Taught Courses VARCHAR(50) 
                    )
                """)
class Student_Master:
    def __init__(self):
        self.stu_id = ""
        self.stu_name = ""
        self.stu_major = ""
        self.stu_courses = ""
        self.stu_cgpa = ""
    def add_student(self):
        self.stu_id = input("Enter Student ID: ")
        self.stu_name = input("Enter Student Name: ")
        self.stu_major = input("Enter Student Major: ")
        self.stu_courses = input("Enter Student Courses: ")
        self.stu_cgpa = input("Enter Student GPA: ")
        sql = "INSERT INTO Student VALUES (%s,%s,%s,%s,%s)"
        values = (self.stu_id, self.stu_name, self.stu_major, self.stu_courses, self.stu_cgpa)
        mycursor.execute(sql, values)
        mydb.commit()
        print("Student created")


class Faculty_Master:
    def __init__(self):
        self.fac_id = ""
        self.fac_name = ""
        self.fac_department = ""
        self.fac_teaches_courses = ""
    def add_faculty(self):
        self.fac_id = input("Enter Faculty ID: ")
        self.fac_name = input("Enter Faculty Name: ")
        self.fac_department = input("Enter Faculty Department: ")
        self.fac_teaches_courses = input("Enter taught Courses: ")
        sql = "INSERT INTO Faculty VALUES (%s,%s,%s,%s)"
        values = (self.fac_id, self.fac_name, self.fac_department, self.fac_teaches_courses,)
        mycursor.execute(sql, values)
        mydb.commit()
        print("Faculty created")

print("1. Create Student")
print("2. Create Faculty")