# n = int(input("Enter row number"))
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         if j>i:
#             print(" ",end="")
#         elif i==n or i==j:
#             print("*",end=" ")
#     print()




#Hollow Reverse Triangle pattern
n = int(input("Enter row number"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if (n-i+1==j) or i==1 :
            print("*",end=" ")
        else:
            print(" ",end="")
    for j in range(n,0,-1):
        if i==j:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()