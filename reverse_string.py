reverse=input("enter the reverse word")
i = len(reverse)-1
word=""
while i>0:
    word=word+reverse[i]
    i = i - 1
print(word)
