class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def add_money(self, amount):
        self.amount = amount
        self.balance += amount
        return self.balance

    def withdrawal_money(self, amount):
        self.amount = amount
        self.balance -= amount
        return self.balance

test = Account('Gr', 500)

cur_balance = test.add_money(1000)

print(cur_balance)

cur_balance = test.withdrawal_money(700)

print(cur_balance)