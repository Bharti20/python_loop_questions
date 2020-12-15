word="I Love"
index=0
count=0
while index<len(word):
    if word[index].isupper():
        count=count+1
    index=index+1
print(count)