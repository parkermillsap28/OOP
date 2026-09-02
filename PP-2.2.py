while (1):
    print("1 Addition")
    print("2 Subtraction")
    print("3 Mulitply")
    print("4 Divide")
    print("5 Exit")
    choice = input("Enter your choice:")

    if choice == "1":
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        sum = n1 + n2
        print(sum)
    elif choice == "2":
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        diff = n1 - n2
        print(diff)
    elif choice == "3":
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        prod = n1 * n2
        print(prod)
    elif choice == "4":
        n1 = int(input("Enter first number:"))
        n2 = int(input("Enter second number:"))
        quot = n1 / n2
        print(quot)
    elif choice == "5":
        exit()
    else:
        print("Please enter a valid number")