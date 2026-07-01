n = int(input("Enter the number: "))
for i in range(1,n+1):
    a = 1
    for j in range(65,65+i):
        ch = chr(j)
        if i%2!=0:
            print(a,end="")
            a+=1
        else:
            print(ch,end='')
    print()