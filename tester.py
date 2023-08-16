from BankAccount import BankAccount
from CurrentAccount import CurrentAccount
from SavingAccount import SavingAccount


account1 = BankAccount(123456789, 1000)
account1.deposit(500)
account1.show_balance()
account1.withdraw(100)
account1.show_balance()


account2 = SavingAccount(987654321, 1000)
account2.deposit(500)
account2.show_balance()
account2.apply_interest(100)
account2.show_balance()


account3 = CurrentAccount(12345678,1000)
account3.deposit(500)
account3.show_balance()
account3.curwithdraw(100)
account3.show_balance()


