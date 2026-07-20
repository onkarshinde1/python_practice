def rebind(x):
    x = [100, 200, 300]
    print(f"Inside function = {x}")


nums = [1, 2, 3]
rebind(nums)
print(f"Outside function = {nums}")
