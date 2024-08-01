n= int(input("Enter the row number"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=i and (i==1 or i==j or j==n):
            print("*",end=" ")
        else:
            print(" ", end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+1):
        if j>=i and (i==1 or i==j or j==n):
            print("*",end=" ")
        else:
            print(" ", end="")
    print()