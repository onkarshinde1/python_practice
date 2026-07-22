class InsufficientFundsError(Exception):
    pass


def withdraw_money(balance, withdraw_amount):
    if withdraw_amount > balance:
        raise InsufficientFundsError("Not enough balance")
    print(f"Remaning balance = {balance-withdraw_amount}")


try:
    withdraw_money(1000, 5000)
except InsufficientFundsError as e:
    print(f"Error name = {type(e).__name__}")
    print(f"error = {e}")
except Exception as e:
    print(f"Error name = {type(e).__name__}")
    print(f"error = {e}")
