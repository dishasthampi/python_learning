n= int(input("Enter number of rows"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print("*",end=" ")
        else:
            print("",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()