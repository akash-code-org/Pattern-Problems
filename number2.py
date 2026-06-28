n = int(input("Enter the number: "))
for i in range(1,n+1,2):
    a = 1
    for j in range(1,i+1,2):
        print(a,end="")
        a+=2
    print()