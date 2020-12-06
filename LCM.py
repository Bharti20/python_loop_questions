a=int(input("enter"))
b = int(input("enter"))
i = 2
while a>0:
    if i%b==0 and i%a==0:
        print("LCM",i)
        break
    i =i+1
      