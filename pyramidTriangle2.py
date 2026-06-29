n = int(input("Enter the number: "))
nst = 1
nsp = 3
for i in range(1,n+1):
    for k in range(1,nsp+1):
        print(' ',end="")
    nsp-=1
    for j in range(1,nst+1):
        print('*',end="")
    nst+=3
    print()

# eys code mein extra variable wali aproach use ho rahi he