n= int(input("Enter the row number"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if i>=j:
            print(i,end=" ")
        else:
            print(" ", end="")
    print()