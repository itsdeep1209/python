class Account:

    def __init__(self, an, hn, bal):
        self.account_number = an
        self.holders_name = hn
        self.balance = bal

# They are invoke automatically on certain action

    def __str__(self):
        return f"{self.account_number} {self.holders_name} {self.balance}"

    def __repr__(self):
        return f"Account({self.account_number}, \"{self.holders_name}\", {self.balance})"

    # Methods

    def print_details(self):
        print( f"Account Number: {self.account_number:010d}\nHolder's name: {self.holders_name}\nBalance: {self.balance:.2f}")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

guido = Account(100101 , " Guido" , 1000.23463)

repr = repr(guido)
print(repr)

s = str(guido)
print(s)

two = eval(repr)
print(two)