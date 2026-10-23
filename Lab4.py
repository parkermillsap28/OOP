import pickle
class Customer:
    def __init__(self):
        self.cid = ""
        self.cname = ""
        self.acc_no = ""
        self.balance = 0
        self.credit_card = []
        self.beneficiary_amount = 0
    def create_customer(self):
        self.cid = input("Enter customer id: ")
        self.cname = input("Enter customer name: ")
        self.acc_no = input("Enter customer account number: ")
        self.balance = input("Enter customer balance: ")
    def add_balance(self):
        new_balance = int(input("Enter balance to add: "))
        self.balance = self.balance + new_balance
        print("New balance is: ", self.balance)
    def transfer_funds(self):
        pass
    def assign_card(self):
        card = input("Enter card number: ")
        customerfile1 = open("customer.dat", "ab")
        for cust_card in customerfile1:
            if card == Card.card_no:
                self.credit_card.append(cust_card)
    def display_customer_info(self):
        customer_file1 = open("customer.dat", "rb")
        while (1):
            try:
                customer = pickle.load(customer_file1)
                print("Customer ID: ", customer.cid,"| Customer name: ", customer.cname,"| Customer account number: ", customer.acc_no,"| Customer balance: ", customer.balance,"| Customer credit card: ", customer.credit_card)
            except EOFError:
                break



class Card:
    def __init__(self):
        self.card_no = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = ""
    def create_card(self):
        self.card_no = input("Enter card number: ")
        self.cvv = input("Enter cv number: ")
        self.expiry_date = input("Enter expiry date: ")
        self.balance = input("Enter balance: ")
    def display_card_info(self):
        card_file1 = open("card.dat", "rb")
        while (1):
            try:
                card = pickle.load(card_file1)
                print("Card NO: ", card.card_no,"| Card CVV: ", card.cvv,"| Card Expiry Date: ", card.expiry_date,"| Card balance: ", card.balance)
            except EOFError:
                break

Cust = Customer()
creditcard = Card()
while 1:
    print("1. Create Customer")
    print("2. Create Credit Card")
    print("3. Transfer Funds")
    print("4. Assign Cards")
    print("5. Display Customer Information")
    print("6. Display Credit Card Information")
    print("7. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        Cust.create_customer()
        customer_file = open("customer.dat", "ab")
        pickle.dump(Cust, customer_file)
        customer_file.close()
        print("Customer created successfully")
    if choice == "2":
        creditcard.create_card()
        credit_file = open("credit_card.dat", "ab")
        pickle.dump(creditcard, credit_file)
        credit_file.close()
        print("Credit card created successfully")
    if choice == "3":
        pass
    if choice == "4":
        Cust.assign_card()
    if choice == "5":
        Cust.display_customer_info()
    if choice == "6":
        Card.display

