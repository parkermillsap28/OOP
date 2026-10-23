AllCustomers = []
AllCreditCards = []
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
        self.balance = int(input("Enter customer balance: "))
    def add_balance(self):
        target_customer = input("Enter customer id: ")
        for customer in AllCustomers:
            if customer.cid == target_customer:
                new_balance = int(input("Enter balance to add: "))
                customer.balance = customer.balance + new_balance
                print("New balance is: ", self.balance)
            else:
                print("Invalid customer ID")
    def transfer_funds(self):
        sender_id= input("Enter the customer's id that is transferring funds: ")
        receiver_id = input("Enter customer's id that is receiving funds: ")
        transfer = int(input("Enter transfer amount: "))
        for customer in AllCustomers:
            if customer.cid == sender_id:
                sender_id = customer
                if sender_id.balance > 0:
                    customer.balance = customer.balance - transfer
                    print("New balance for sender is:", sender_id.balance)
                else:
                    print("Insufficient funds")
        for customer in AllCustomers:
            if customer.cid == receiver_id:
                receiver_id = customer
                customer.balance = customer.balance + transfer
                print("New balance for receiver is:", receiver_id.balance)

    def assign_card(self):
        target_card = input("Enter card number: ")
        target_cid = input("Enter customer id: ")
        for card in AllCreditCards:
            if card.card_no == target_card:
                for customer in AllCustomers:
                    if customer.cid == target_cid:
                        customer.credit_card.append(target_card)
                        print(target_card, "now assigned to:", target_cid)

    def display_customer_info(self):
        for customer in AllCustomers:
            print("Customer ID: ", customer.cid)
            print("Customer Name: ", customer.cname)
            print("Customer Account Number: ", customer.acc_no)
            print("Customer Balance: ", customer.balance)
            print("Customer Card Number: ", customer.credit_card)



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
       for card in AllCreditCards:
            print("card number: ", card.card_no)
            print("cv number: ", card.cvv)
            print("expiry date: ", card.expiry_date)
            print("balance: ", card.balance)

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
        new_cust = Customer()
        new_cust.create_customer()
        AllCustomers.append(new_cust)
        print("Customer created successfully")
    elif choice == "2":
        new_card = Card()
        new_card.create_card()
        AllCreditCards.append(new_card)
        print("Credit card created successfully")
    elif choice == "3":
        Cust.transfer_funds()
    elif choice == "4":
        Cust.assign_card()
    elif choice == "5":
        Cust.display_customer_info()
    elif choice == "6":
        creditcard.display_card_info()
    elif choice == "7":
        exit()
    else:
        print("Invalid input")
