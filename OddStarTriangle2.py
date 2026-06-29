n = int(input("Enter the number: "))
nst = 1
for i in range(1,n*2-1):
    for j in range(1,nst+1):
        print('*',end="")
    nst+=2
    print()