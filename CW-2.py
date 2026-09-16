while 1:
    print("1 Create a list")
    print("2 Add an element to list")
    print("3 Remove an element from list")
    print("4 Replace an element the list")
    print("5 Sort list")
    print("6 Print list")
    print("7 Exit")
    choice = input("enter your choice")
    if choice == "1":
        list1 = []
        print("List has been created")
    elif choice == "2":
        add = input("Please enter an element to add. Type q when done adding to list")
        while add != "q":
            list1.append(add)
            add = input("Enter a new element, or type q to stop: ")
        print("List has been updated")
    elif choice == "3":
        sub = input("please enter an element to remove. Type q when done removing from list")
        while sub != "q":
            list1.remove(sub)
            sub = input("Enter a new element, or type q to stop: ")
        print("List has been updated")
    elif choice == "4":
        old_element = input("please enter an element to remove: ")
        new_element = input("please enter an element to add: ")
        index = list1.index(old_element)
        list1[index] = new_element
        print("List has been updated")
    elif choice == "5":
        list1.sort()
        print("List has been updated")
    elif choice == "6":
        print(list1)
    elif choice == "7":
        exit()
    else:
        print("Please enter a valid choice")