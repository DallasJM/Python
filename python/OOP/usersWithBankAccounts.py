class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def withdrawal(self, amount):
        self.account_balance -= amount


dallas = User("dallas", "dallas@python.com")


class BankAccount:
    def __init__(self, int_rate, balance):
        self.int = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        self.balance *= self.int
        return self


discover = BankAccount("7.75%", 2500)
wells = BankAccount("5%", 2000)

discover.deposit(1000).withdraw(3000).yield_interest().display_account_info
