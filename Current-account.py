from BankAccount import BankAccount


class CurrentAccount(BankAccount):
    def __init__(self,num,IniAmount):
        super().__init__(num,IniAmount)
        print(f"congrats... your current account has been created{self._AccNo} ")

    def currentwithdrwal(self,amount):
        amount +=200
        print("charge 100 is applicable for every withdraw")
        self.withdraw(amount)
