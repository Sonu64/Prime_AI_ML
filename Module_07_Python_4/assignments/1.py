class BankAccount:
    def __init__(self, accountNumber, ownerName, balance):
        self.accountNumber = accountNumber
        self.ownerName = ownerName
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of Rs.{amount} Successful ! New Balance is Rs.{self.balance}.")
    def withDraw(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print(f"Withdraw of Rs.{amount} Successful ! New Balance is Rs.{self.balance}.")
        else:
            print(f"Withdraw Failed ! Insufficient Funds (Rs.{self.balance}) to withdraw Rs.{amount}")
    def getBalance(self):
        return self.balance
    
myAccount = BankAccount("SBIN00084237", "Sourakanti Mandal", 1000)
myAccount.deposit(900)
print(f"Current Balance = Rs. {myAccount.getBalance()}")
myAccount.withDraw(500)
myAccount.withDraw(90000)
