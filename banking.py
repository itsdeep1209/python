class Account:

    def __init__(self,an,hn,bal):
        self.account_number = an
        self.holders_name = hn
        self.balance = bal

    def print_details(self):
        print("Account number:", self.account_number)
        print("Holders name:", self.holders_name)
        print("Balance:", self.balance)
        # print("Acoount=", self.account_number, "Holders Name=", self.holders_name , "Balance=", self.balance)
        # print("Account=%5d, Holder Name=%-20s, Balance=%10.2f"%(self.account_number,self.holders_name,self.balance))

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

guido = CurrentAccount(100101, "Guido" , 1000)
guido.withdraw(1)
guido.print_details()

lars = CurrentAccount(100102, "Lars Bak" , 1000)
anders = FixedDeposit(100103, "Anders Hejalberg", 1000)
guido = SavingsAccount(100101, "Guido", 1000)

bank_list = [lars, guido, anders]

for acct in bank_list:
    try:
        acct.withdraw(1000)
        acct.print_details()
    except Exception as err:
        print("Error", acct.holders_name, err)      


class SavingsAccount(Account):
    def __init__(self,an,hn,bal,min_bal):
        # constructor chaining
        super().__init__(an,hn,bal)
        self.minimum_balance = min_bal

def withdraw(Self,amount):
    if self.balance - amount < self.minimum_balance:
        raise Exception("Insufficient balance")
    super().withdraw(amount)

class CurrentAccount(Account):

    def __init__(self,an,hn,bal,od_limit):
      super().__init__(an,hn,bal)
      self.overdraft_limit = od_limit

    def withdraw(self,amount):
        if self.balance - amount < -self.overdraft_limit:
            raise Exception("Overdraft limit reached")
        #self.balance -= amount
        super().withdraw(amount)



