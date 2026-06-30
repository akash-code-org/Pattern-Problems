for i in range(1,4+1):
    for j in range(1,4+1-i):
        print(" ",end=" ")
    for k in range(65,65+i):
        ch = chr(k)
        print(ch,end=" ")
    print()