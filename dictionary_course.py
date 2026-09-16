while 1:
    print("1 Create a new course list")
    print("2 Add to a course")
    print("3 Delete a course")
    print("4 Replace courses")
    print("5 Display course list")
    choice = input("Please enter your choice: ")
    if choice == "1":
        courselist = {}
        print("Course list has been created")
    elif choice == "2":
        courselist.update({"course1" : input("Please enter course name: ")})
        print("Course has been added")
    elif choice == "3":
        del courselist[input("Please enter course name: ")]
        print("Course has been deleted")
    elif choice == "4":

