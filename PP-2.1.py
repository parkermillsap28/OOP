student = input("What is your name?")
Course1 = int(input("Grade for course one"))
Course2 = int(input("Grade for course two"))
Course3 = int(input("Grade for course three"))
total =  Course1 + Course2 + Course3
percentile = (total/300) * 100
if percentile <= 100 and percentile >= 90:
    print("Grade A")
    print(percentile)
elif percentile < 90 and percentile >= 80:
    print("Grade B")
    print(percentile)
elif percentile < 80 and percentile >= 70:
    print("Grade C")
    print(percentile)
elif percentile < 70 and percentile >= 60:
    print("Grade D")
    print(percentile)
elif percentile < 60:
    print("Grade F")
    print(percentile)
