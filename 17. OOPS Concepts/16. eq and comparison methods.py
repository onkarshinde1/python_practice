class Money:
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __le__(self, other):
        return self.amount <= other.amount


a = Money(80)
b = Money(100)

print(a == b)
print(a < b)
print(a <= b)
# print(a > b)
