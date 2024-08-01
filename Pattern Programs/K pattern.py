n=int(input("Enter row number"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if i<=j:
            print("*", end=" ")
        else:
            print(" ",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n,0,-1):
        if i<=j:
            print("*", end=" ")
        else:
            print(" ",end="")
    print()