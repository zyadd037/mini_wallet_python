class InsufficientFundsError(Exception):
    pass

class wallet:
    def __init__(self,initial_balance):
        self.balance = initial_balance

    def withdraw(self,amount):
        self.amount = amount
        if amount > self.balance:
            raise InsufficientFundsError (f"Ops Cannot deal with widthdraw {self.amount} , check your current balance {self.balance} !")

        self.balance -= amount
        print(f"Your remaining balance after Withdrawal of funds is {self.balance} :) ")

#Testing
my_wallet = wallet(5000) 

try:
    my_wallet.withdraw(5500) # 4000

    
except InsufficientFundsError as e:
    print(f" Ops operation faild : {e} !")
    
        

