n = int(input("enter the number"))
i =2
sum= 0
while i<n:
    if (n%i==0):
        s=n//i
        sum = sum+s
    i = i+1
if sum+1==n:
    print("perfect no")
else:
    print("not perfect")
    
