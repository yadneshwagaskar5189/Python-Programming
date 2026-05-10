class Bankaccount:
    def __init__(self, account_number, owner_name, Balance=1000):
        self.account_number = account_number
        self.Balance = Balance
        self.owner_name = owner_name
    def deposit(self, amount):
        #amount=int(input("Enter amount ot be Deposit:-"))
        if amount>0:
            self.Balance+=amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount. Please enter a positive value.")
    def withdraw(self, amount):
        #amount=int(input("Enter amount ot be withdrawn:-"))
        if amount>0:
            self.Balance-=amount
            print("Amount withdrawn successfully")
        else:
            print("Invalid amount. Please enter a positive value.")
    def display(self):
        print("Account number:-",self.account_number)
        print("Balance:-",self.Balance)
        print("Owner name:-",self.owner_name)
b1=Bankaccount(108765,"Priyanshu")
b1.deposit(5000)
b1.withdraw(2000)
b1.display()
