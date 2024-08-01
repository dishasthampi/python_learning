# n= int(input("Enter number of rows"))
# for i in range(1,n+1):
#     for j in range(n,0,-1):
#         if j<=i:
#             print("*",end=" ")
#         else:
#             print("",end=" ")
#     print()
# for i in range(n-1,0,-1):
#     for j in range(n,0,-1):
#         if j<=i:
#             print("*",end=" ")
#         else:
#             print(" ",end="")
#     print()

n = int(input("Enter number of rows"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1,i+1):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
#     for j in range(n-i,0,-1):
#         print(" ", end="")
#     for j in range(i,0,-1):
#         print("*", end=" ")
#     print()
    for j in range(1,n-i+1):
        print(" ", end="")
    for j in range(1,i+1):
        print("*", end=" ")
    print()
