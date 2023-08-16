class BankAccount:
    __account_number=None
    __balance=None

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def show_balance(self):
        print(str(self.account_number)+" Your balance is: Rs{} ".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

    def transfer(self, to_account, amount, bankAccount):

        self.withdraw(amount)
        bankAccount.deposit(amount)



