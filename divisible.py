n= int(input("kitni bar input lena hai"))
while n>0:
    a = int(input("enter the number"))
    if a%3==0 and a%5==0:
        print("Fizz-Buzz")
    elif a%3==0:
        print("fizz")
    elif a%5==0:
        print("Buzz")
    elif a%3!=0 and a%5!=0:
        print("Buzz-Fizz")
    n = n-1