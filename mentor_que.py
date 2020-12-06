num = int(input("enter the number"))
sum=0
while num>=1:
    x = num%10
    sum = sum + x
    num = num//10
print(sum)



