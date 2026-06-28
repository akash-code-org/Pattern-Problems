n = int(input("Enter the number: "))
# a = n
for i in range(1,n+1):
    for j in range(1,n+2-i): # a +1
        print("*",end="")
    print()
    # a-=1
# eys rectangle ko ek extra variable use kr ke variable ko 1 se decrement kr ke display krwa sakti he
# uper code ke sath extra variable wala example deya gaya he