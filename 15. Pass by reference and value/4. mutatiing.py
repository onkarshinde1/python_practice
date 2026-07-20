def mutate(x):
    # x[0] = 100
    x.append(100)
    print(f"Inside function = {x}")


nums = [1, 2, 3]
mutate(nums)
print(f"Outside function = {nums}")
