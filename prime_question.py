# n = int(input("enter the number"))

# only for one number
# i = 1
# count=0
# while i<=n:
#     if n%i==0:
#         count=count+1
#     i = i+1
# if count==2:
#     print(n, "is prime number")
# else:
#     print("not prime number")

# this code for till user input

n = int(input("enter the number"))
i = 2
while i<=(n*2)+1:
    j=1
    count=0
    while j<=(n*2)+1:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        print(i)
    i = i+1
