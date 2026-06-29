n = int(input("Enter the number: "))
for i in range(1,n*2-1):
    for j in range(1,i*2-1+1):
        print('*',end="")
    print()