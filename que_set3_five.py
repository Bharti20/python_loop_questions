i = 1
sum = 0
while i<=11:
	user=int(input("enter the weight"))
	sum = sum + user
	i = i + 1
print(sum)
avrage = sum//11
print(avrage)
if avrage%5==0:
	print("yes")
else:
	print("no")
