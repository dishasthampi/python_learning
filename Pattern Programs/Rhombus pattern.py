# n= int(input("Enter a row number"))
# for i in range(1,n+1):
#     for j in range(1,n+1+i):
#         if j>=i:
#             print("*",end="")
#         else:
#             print("",end=" ")
#     print()

n = int(input("Enter a row number"))
for i in range(1,n+1):
    for j in range(1,n+i-1):
        print(" ", end="")
    for j in range(1,n+1):
        print("*", end=" ")
    print()
