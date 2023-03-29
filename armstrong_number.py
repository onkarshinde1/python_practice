num=input("Enter the number:")
digit=len(num)
print(digit)
number=list(num)
print(number)
sum=0
for x in number:
    n=int(x)
    p=n**digit
    sum=sum+p
finalnum=int(num)
if finalnum == sum:
    print("Given number is armstrong")
else:
    print("Given number is not a armstrong")