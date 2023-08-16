
from BankAccount import BankAccount
from CurrentAccount import CurrentAccount
from SavingAccount import SavingAccount

Bank = BankAccount(1112, 500)
Bank.DisplayBalance()
Bank.withdraw(100)
Bank.DisplayBalance()
Bank.deposit(700)
Bank.DisplayBalance()

print("========================================")

Save = SavingAccount(1111,1000)
Save.DisplayBalance()
Save.savingdeposit(3000)
Save.DisplayBalance()
Save.withdraw(4000)
Save.DisplayBalance()

print("========================================")

Cur = CurrentAccount(1113,100000)
Cur.DisplayBalance()
Cur.currentwithdrwal(99800)
Cur.DisplayBalance()

print("========================================")

T1 =BankAccount(1114,3000)
T1.DisplayBalance()
T1.Transfer(500, Bank)
T1.DisplayBalance()
Bank.DisplayBalance()
