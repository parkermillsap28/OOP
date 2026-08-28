number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
number3 = int(input("enter third number"))
if number1 > number2 and number3:
    print ("number1 is the biggest")
elif number2 > number1 and number3:
    print("number2 is the biggest")
elif number3 > number1 and number2:
    print("number3 is the biggest")
elif number1 == number2 or number3:
    print("invalid numbers")

