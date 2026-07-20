import copy


def add_item(x):
    x = copy.deepcopy(x)
    x.append(100)
    print(f"Inside function = {x}")


nums = [1, 2, 3]
add_item(nums)
print(f"Outside function = {nums}")
