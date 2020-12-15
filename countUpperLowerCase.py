word="I Love InDia"
index=0
upper_case=0
lower_case=0
for index in range(len(word)):
    if (ord(word[index]) >= 65 and ord(word[index]) <= 90):
        upper_case=upper_case+1
    elif (ord(word[index])>=97 and ord(word[index])<=122):
        lower_case=lower_case+1
    index=index+1
print(upper_case)
print(lower_case) 