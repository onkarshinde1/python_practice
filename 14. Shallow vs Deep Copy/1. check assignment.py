original = [1, 2, 3]
copy = original

copy.append(100)
print(id(original))
print(id(copy))

print(original is copy)
print(original == copy)

print(copy)
print(original)

a = [4, 5, 6]
b = [4, 5, 6]
print(a is b)
print(a == b)
