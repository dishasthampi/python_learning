# n = int(input("Enter row number"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         for k in range(1, n-i+1):
#             print(" ",end="")
#         print("*",end=" ")
#     print()

# n = int(input("Enter row number"))
# for i in range(1,n+1):
#     for j in range(n+1-i,1,-1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

n = int(input("Enter row number"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j<=i:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()