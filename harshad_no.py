num = int(input("enter  "))
sum = 0
i = num
while i>0:
    a = i%10
    sum = sum+a
    i=i//10
if num%sum==0:
        print("harsad number hai")
else:
    print("no harsad")