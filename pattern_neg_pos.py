pattern = 1
while pattern<=100:
    if pattern%2==0:
          print(-pattern, end=" ")
    else:
        print(pattern, end=" ")
    if pattern%10==0:
      print(sep="\n")
    pattern = pattern + 1

