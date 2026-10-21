MyCategories = []

class Calculator:
    def __init__(self):
        self.user_income = int(input("What is your current income? "))
        self.budget = self.user_income
        #previous amount leftover or new amount
    def calc_add(self):
        while self.user_income > 0:
            print(MyCategories)
            category = input("What category should be edited?")
            if category == "Exit":
                break
            for cat in MyCategories:
                if cat.category == category:
                    using = cat
                else:
                    using = "not found"
            if using in MyCategories:
                amount = int(input("Please enter the amount to be added: "))
                self.budget = self.budget - amount
                using.budget = using.budget + amount

            else:
                print("Please enter a valid category")
    def calc_subtract(self):
        if self.user_income > 0:
            print(MyCategories)
            if category in MyCategories:
                amount = int(input("Please enter the amount to be taken: "))
                self.user_income = self.user_income + amount
                self.budget = self.budget - amount

            else:
                print("Please enter a valid category")
class Category:
    def __init__(self):
        self.category = ""
        self.budget = 0
    def new_category(self):
        new_category = input("Please enter a new category: ")
        self.category = new_category
        self.budget = int(input("Please enter the budget: "))
    def display_categories(self):
        print(self.category)
        print(self.budget)

Calc = Calculator()



while (1):
    print("Please choose one of the following options:")
    print("1. Make a new category")
        #subtract from income and add to category
    print("2. Add to a category")
        #subtract from category and add to income
    print("3. Subtract from a category")
    print("4. Display categories")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        category = Category()
        category.new_category()
        MyCategories.append(category)
    if choice == "2":
        Calc.calc_add()
    if choice == "3":
        category = input("What category should be edited?")
        for category in MyCategories:
            category.calc_subtract()
    if choice == "4":
        for category in MyCategories:
            category.display_categories()
    if choice == "5":
        exit()

