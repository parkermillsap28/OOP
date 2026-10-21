class Calculator:
    def __init__(self):
        self.user_income = input("What is your current income? ")
        self.budget_category = None
    def calc_add(self):
        while self.user_income > 0:
            print(MyCatagories)
            category = input("What category should be edited?")
            if category in MyCatagories:
                amount = int(input("Please enter the amount to be added"))
                self.user_income = self.user_income - amount
                self.budget_category = category + amount

            else:
                print("Please enter a valid category")
    def calc_subtract(self):
        if self.user_income > 0:
            pass
class Category:
    def __init__(self):
        self.category = ""
    def new_category(self):
        new_category = input("Please enter a new category")
        self.category = new_category
        MyCatagories.append(new_category)


MyCatagories = []
category = Category()
while (1):
    print("Please choose one of the following options:")
    print("1. Add to a category")
        #subtract from income and add to category
    print("2. Subtract from a category")
        #subtract from category and add to income
    print("3. Make a new category")
    print("4. Exit")