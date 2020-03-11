
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
d = User("dad", "d@python.com")
m = User("sum", "m@python.com")

dallas.make_deposit(100)
dallas.make_deposit(600)
d.make_deposit(75)
d.withdrawal(10)
dallas.withdrawal(400)
print(dallas.account_balance)
print(d.account_balance)
