n = int(input("enter the number"))
a = int(input("enter the number"))
i = 2
c=0
while i<=a:
    if n%i==0 and a%i==0:
        c=i
    i = i+1
print("HCF",c)
