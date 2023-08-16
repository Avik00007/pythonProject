from BankAccount import BankAccount


class SavingAccount(BankAccount):


    def __init__(self,num,IniAmount):
        super().__init__(num,IniAmount)
        print(f"congrats..your saving account has been is created {self._AccNo}")

    def savingdeposit(self, amount):
        intrest = amount * 3/100
        amount += intrest
        print(f"{intrest} intrest is added in your account ")
        self.deposit(amount)
