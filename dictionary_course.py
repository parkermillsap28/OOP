i = 1
while 1:
    print("1 Create a new course list")
    print("2 Add to a course")
    print("3 Delete a course")
    print("4 Replace courses")
    print("5 Display course list")
    print("6 Exit")
    choice = input("Please enter your choice: ")

    if choice == "1":
        courselist = {}
        print("Course list has been created")
    elif choice == "2":
        course_name = input("Please enter course name: ")
        courselist.update({"course_name"+str(i) : course_name})
        i = i + 1
        print("Course has been added")
    elif choice == "3":
        del courselist[input("Please enter course_name#: ")]
        print("Course has been deleted")
    elif choice == "4":
        courselist[input("Please enter course_name#: ")] = input("Please enter new course name: ")
        print("Course has been updated")
    elif choice == "5":
        print(courselist)
    elif choice == "6":
        exit()
    else:
        print("Please enter a valid choice")


