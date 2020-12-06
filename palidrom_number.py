n=int(input("Enter number:")) 
i=n 
rev=0 
while(n>0):
    a=n%10 
    rev=rev*10+a 
    n=n//10 
if(i==rev):
    print("palindrome")
else: 
    print("not palindrome") 