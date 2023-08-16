from BankAccount import BankAccount


class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)


    def  curwithdraw(self, amount):
        amount+=200
        print("200 charge is taken for each transaction")
        self.withdraw(amount)
