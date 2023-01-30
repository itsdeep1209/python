class SavingsAccount(Account):

    def withdraw(self,amount):
        if self.balance - amount < 500:
            raise Exception("Insufficient balance")
        self.balance -= amount

        
class CurrentAccount(Account):

    def withdraw(self , amount):
        if self.balance + amount > 5000:
            raise Exception("Overdraft limit reached")
        self.balance -= amount

class FixedDeposit(Account):
    def withdraw(self, amount):
        raise Exception("Cannot with draw from FD")

    def print_details(self):
        print("Account number:", self.account_number)
        print("Holders name:", self.holders_name)
        print("Balance:", self.balance)
        
guido = FixedDeposit(100101, "Guido" , 1000)
guido.withdraw(1)
guido.print_details()