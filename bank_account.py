print("welcome!!!!")
class BankAccount:
    _CurBal = None
    _AccNo = None
    def __init__(self,num,IniAmount):
        self._CurBal = IniAmount
        self._AccNo = num

    def DisplayBalance(self):
        print(f"{self._AccNo}your account balence is {self._CurBal}")

    def deposit(self, amount):
        self._CurBal += amount
        print(f"{amount} is deposited in your account: {self._AccNo}")

    def ChkBal(self,amount):
        if self._CurBal < amount:
            return False
        else:
            return True

    def withdraw(self, amount):
        if self.ChkBal(amount):
            self._CurBal -= amount
            print (f"{amount}is withdraw from your account: {self._AccNo}")

    def Transfer(self,amount, BankAccount):
        self.withdraw(amount)
        BankAccount.deposit(amount)
