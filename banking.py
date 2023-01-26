class Account:

    def __init__(self,an,hn,bal):
        self.account_number = an
        self.holders_name = hn
        self.balance = bal

    def print_details(self):
        print("Account number:", self.account_number)
        print("Holders name:", self.holders_name)
        print("Balance:", self.balance)

    def deposit(self, amount , currency):
        self.balance += amount
     
        

guido = Account(100101, "Guido", 100000)
guido.print_details()
guido.deposit(5000)