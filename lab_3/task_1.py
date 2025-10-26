#Задания Вариант 1  Класс BankAccount
class BankAccount:
    accounts_quantity = 0
    MIN_BALANCE = 100
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
        BankAccount.accounts_quantity += 1

    def __str__(self):
        return f'номер счета:{self.account_number},баланс:{self.balance},минимальный баланс:{self.MIN_BALANCE}'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount <= self.MIN_BALANCE:
            print('операция отклонена')
        else:
            self.balance -= amount

    def check_balance(self):
        print(f'balance:{self.balance}')
acc = BankAccount('1',50)
acc.deposit(100)
acc.check_balance()
print(acc)