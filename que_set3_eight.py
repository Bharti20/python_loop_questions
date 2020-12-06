i = 1
while i <=10:
    user=int(input("enter the number"))
    if user==5:
        print("Waah! aapne number guess kar liya")
        Break
    elif user<5:
        print("Aapka number chota hai! Ek aur bar try kijiye")
    elif user>5:
        print("Aapka number bada hai! Phir se koshish kijiye")
    i = i + 1
else:
    print("Try next time, aapne guess nahi kiya")