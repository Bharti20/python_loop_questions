i=2
total_prime_no=0
while i<=100:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        print(i)
        total_prime_no=total_prime_no+1
    i=i+1
print()
print("total prime numbers",total_prime_no)