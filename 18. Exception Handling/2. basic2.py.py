try:
    num1 = int(input("Enter number 1 = "))
    num2 = int(input("Enter number 2 = "))
    print(f"num1/num2 = {num1/num2}")
except ZeroDivisionError:
    print("Cannt divide by zero, please enter proper integers")
except ValueError:
    print("Please enter proper integers")
except:
    print("Some error occurred")
