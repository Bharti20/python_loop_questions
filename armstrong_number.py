n = int(input("enter the number"))
sum = 0
i = n
while i>0:
    b=(i%10)**3
    sum = sum +b
    i = i//10
if n==sum:
    print("armstrong")
else:
    print("not")
