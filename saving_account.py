from BankAccount import BankAccount


class SavingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)



    def apply_interest(self,amount):
        interest_rate=amount*3/100
        amount+=interest_rate
        print(str(self.account_number)+" the interest given is " +str(interest_rate)+"%")
        self.deposit(amount)
