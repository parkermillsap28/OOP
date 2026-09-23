n = 0
mystudents ={}

def add_student():
    name = input("Please enter student name: ")
    Lab1 = int(input("Please enter grade for Lab 1: "))
    Lab2 = int(input("Please enter grade for Lab 2: "))
    Lab3 = int(input("Please enter grade for Lab 3: "))
    Lab4 = int(input("Please enter grade for Lab 4: "))
    Lab5 = int(input("Please enter grade for Lab 5: "))
    total = Lab1 + Lab2 + Lab3 + Lab4 + Lab5
    percent = (total/50) * 100
    average = total/5
    mystudents.update (
        {"s"+str(n) : {
            "stu_name": name,
            "stu_lab1": Lab1,
            "stu_lab2": Lab2,
            "stu_lab3": Lab3,
            "stu_lab4": Lab4,
            "stu_lab5": Lab5,
            "total": total,
            "percent": percent,
            "average": average

                    }
        }

    )
i = n + 1

def delete_student():
    del mystudents[input("Please enter s#: ")]
    print("student has been deleted")

while (1):
    print("1 Add a student")
    print("2 Delete a student")
    print("3 Display students")
    print("4 Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
        print("Student added successfully")
    elif choice == "2":
        delete_student()
        print("Student deleted successfully")
    elif choice == "3":
        print(mystudents)
    elif choice == "4":
        exit()
    else:
        print("Please enter a valid choice")
