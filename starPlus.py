n = int(input("Enter the number: "))

#a = n // 2 + 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        a = n // 2 + 1
        if i == a or j == a:
            print("*", end="")
        else:
            print(" ", end="")
    print()