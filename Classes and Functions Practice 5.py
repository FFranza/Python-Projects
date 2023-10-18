account_number = 23123124
account_holder = "Alice"
initial_balance = 500
amount = 300

class Bankaccount:
    def __init__(self, account_number, account_holder, initial_balance):
        self.accnumber = account_number
        self.accholder = account_holder
        self.inibalance = initial_balance
    
    def deposit(self, amount):
        self.amount = amount # Insert amount
        
        self.inibalance += self.amount
        return self.inibalance
    
    def withdraw(self, amount):
        self.amount = amount
        if self.inibalance < amount: 
            print("You have insufficient amount of funds and unable to withdraw")
            return self.inibalance
        else:
            self.inibalance -= amount
        return self.inibalance

# Tie class to variable
bacc = Bankaccount(account_number, account_holder, initial_balance)

# Tie functions of variables to variables
deposited_balance = bacc.deposit(amount)
print(f"Your new deposited balance is {deposited_balance}")
withrdawn_balance = bacc.withdraw(amount)
print(f"Your new withdrawn balance is {withrdawn_balance}")
    