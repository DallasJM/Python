class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def withdrawal(self, amount):
        self.account_balance -= amount

    def display_users_balance():
        self.account_balance = amount


dallas = User("dallas", "dallas@python.com")
d = User("dad", "d@python.com")
m = User("sum", "m@python.com")

dallas.make_deposit(100).make_deposit(
    600).withdrawal(62).display_users_balance()
