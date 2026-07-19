import copy

original = [54, 12, 76, [67, 19, 20, 78], 98, 100, 3]
# shallow = original.copy()
shallow = copy.deepcopy(original)


print(id(original))
print(id(shallow))

shallow[3][1] = 999
shallow[6] = 1000

print(original)
print(shallow)
