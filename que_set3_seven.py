i = 1
while i <=5:
    user=int(input("enter the number"))
    if user==5:
        print("congratulations! aapne guess kar liya")
        break
    elif user!=5:
        print("Try agin")
    i = i + 1
else:
    print("Try next time, aapne guess nahi kiya")
