while (1):
    print("1 to Calculate Area of Square")
    print("2 to Calculate Volume of Cube")
    print("3 to Calculate Area of Circle")
    print("4 to Calculate Circumference of Circle")
    print("5 to Exit")
    choice = input("Enter your choice:")
    if choice == "1":
        len = int(input("Please input length:"))
        wid = int(input("Please input width:"))
        areas = len * wid
        print("Area of Square is ", areas)
    elif choice == "2":
       len = int(input("Please input length:"))
       wid = int(input("Please input width:"))
       hei = int(input("Please input height:"))
       vol = len * wid * hei
       print("Area of Cube is ", vol)
    elif choice == "3":
        rad = int(input("Please input radius:"))
        areac = 3.14 * rad * rad
        print("Area of Circle is ", areac)
    elif choice == "4":
        rad = int(input("Please input radius:"))
        circ = 2 * 3.14 * rad
        print("Circumference of Circle is ", circ)
    elif choice == "5":
        exit()
    else:
        print("Please enter a valid choice")


