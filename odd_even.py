i = 1
count = 0
count1 = 0
while i <=10:
    if i %2!=0:
        print("odd",i)
        count = count+1
    if i %2==0:
        print("even",i)
        count1 = count1+1
    i = i +1
print(count)
print(count1)