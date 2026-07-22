class Bank:
    def __init__(self, name: str, balance: int) -> None:
        self.name: str = name
        self.__balance: int = balance

    def deposit(self, amount: int):
        if amount < 0:
            print("Invalid amount")
        else:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


b1 = Bank("Anirudh", 1000)
print(b1.get_balance())
b1.deposit(-1000)
print(b1.get_balance())
print(b1._Bank__balance)
