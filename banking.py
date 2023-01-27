class Account:

    def __init__(self,an,hn,bal):
        self.account_number = an
        self.holders_name = hn
        self.balance = bal

    def print_details(self):
        print("Account number:", self.account_number)
        print("Holders name:", self.holders_name)
        print("Balance:", self.balance)
        print("Acoount=", self.account_number, "Holders Name=", self.holders_name , "Balance=", self.balance)
        print("Account=%5d, Holder Name=%-20s, Balance=%10.2f"%(self.account_number,self.holders_name,self.balance))

    def deposit(self, amount):
        self.balance += amount
     
    def withdrawal(self, amount):
        self.balance -= amount
        

guido = Account(100101, "Guido", 100000)
guido.print_details()
guido.deposit(5000)
guido.print_details()
guido.withdrawal(2000)
guido.print_details()