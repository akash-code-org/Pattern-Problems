n = int(input("Enter the number: "))
for i in range(1,n+1,2):
    for j in range(1,i+1):
        if j%2!=0:
            print(j,end="")
    print()