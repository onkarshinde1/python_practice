import copy

original = [1, 2, 3]
# shallow = original.copy()
shallow = copy.copy(original)


print(id(original))
print(id(shallow))

shallow.append(100)


print(original)
print(shallow)
