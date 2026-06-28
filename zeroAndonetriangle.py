n = int(input("Enter the number: "))
a = 0
for i in range(1,n+1):
    if i%2!=0:
        a = 1
    else:
        a = 0
    for j in range(1,i+1):
        print(a,end="")
        if a==0:
            a = 1
        else:
            a = 0
    print()