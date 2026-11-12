class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print("Name:", self.name)
        print("Balance:", self.balance)


b = Bank("Keerthana", 5000)
b.deposit(2000)
b.withdraw(1000)
b.display()