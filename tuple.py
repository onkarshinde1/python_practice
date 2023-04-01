from ast import Delete


tuple =("roshan",31,58,"nikam")
tuple2 = (5,89,[-70,9])
tuple3 =(tuple,tuple2)
tuple4 =(2,4,6,8)
print(tuple)
print(tuple[2])
print(tuple + tuple2)
print(tuple3)
print(tuple[2:4])
print (len(tuple))
tuple2[2][0]=12
print (tuple2)
print("roshan" in tuple)
print (max(tuple4))
print (min(tuple4))
print (sum(tuple4))
print (sorted(tuple4))
for t in tuple:
    print(t)
del tuple4