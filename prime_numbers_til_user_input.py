num=int(input("enter the number"))
i=2
count=0
while count<num:
    j=1
    count2=0
    while j<=i:
        if i%j==0:
            count2=count2+1
        j=j+1
    if count2==2:
        print(i)
        count=count+1
    i=i+1
