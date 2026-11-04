MyCategories = []
class Calculator:
    def __init__(self):
        self.user_income = int(input("What is your current income? "))
        self.budget = self.user_income
    def calc_add(self):
        while self.user_income > 0:
            print(MyCategories)
            category = input("What category should be edited?")
            if category == "Exit":
                break
            for cat in MyCategories:
                if cat.category == category:
                    using = cat
                    break
            if using in MyCategories:
                amount = int(input("Please enter the amount to be added: "))
                if self.budget - amount < 0:
                    print("Budget cannot be negative")
                    break
                else:
                    self.budget = self.budget - amount
                    using.budget = using.budget + amount

            else:
                print("Please enter a valid category")
    def calc_subtract(self):
        while self.user_income > 0:
            print(MyCategories)
            category = input("What category should be edited?")
            if category == "Exit":
                break
            for cat in MyCategories:
                if cat.category == category:
                    using = cat
                    break
            if using in MyCategories:
                amount = int(input("Please enter the amount to be subtracted: "))
                if using.budget - amount < 0:
                    print("Budget cannot be negative")
                    break
                else:
                    self.budget = self.budget + amount
                    using.budget = using.budget - amount
    def display_income(self):
        print("Starting Income Amount: ", self.user_income)
        print("Budget remaining: ", self.budget)

class Category:
    def __init__(self):
        self.category = ""
        self.budget = 0
        self.weight = 0
    def new_category(self):
        new_category = input("Please enter a new category: ")
        self.category = new_category
        self.budget = int(input("Please enter the starting budget: "))
        self.weight = int(input("Please enter the weight in percent: "))
    def remove_category(self):
        pass
    def display_categories(self):
        print(self.category)
        print(self.budget)
    def update_weights(self):
        wghtdcat = input("Enter a category to be updated: ")
        found = None
        for cat in MyCategories:
            if wghtdcat == cat.category:
                found = cat
                break
        if found:
            new_weight = int(input("Enter new weight in percent: "))
            total = sum(cat.weight for cat in MyCategories) - self.weight + new_weight
            if total > 100:
                print("Cannot add weight---exceeds total income")
            else:
                self.weight = new_weight
        else:
            print("Category not found")

Calc = Calculator()



while (1):
    print("Please choose one of the following options:")
    print("1. Make a new budget category")
    print("2. Add to a category")
    print("3. Subtract from a category")
    print("4. Display categories")
    print("5. Update weights for budget categories")
    print("6. Display remaining income")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        category = Category()
        category.new_category()
        total_weight = sum(cat.weight for cat in MyCategories) + category.weight
        if total_weight > 100:
            print("Cannot add category---exceeds total income")
        else:
            MyCategories.append(category)
            percent = category.weight / 100
            category.budget = category.budget + Calc.user_income * percent
            Calc.budget = Calc.budget - Calc.user_income * percent
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
        for category in MyCategories:
            category.update_weights()
            total_weight = sum(cat.weight for cat in MyCategories) + category.weight
            if total_weight > 100:
                print("Cannot add category---exceeds total income")
            else:
                percent = category.weight/100
                category.budget = category.budget + Calc.user_income * percent
    if choice == "6":
        Calc.display_income()
    if choice == "7":
        exit()

