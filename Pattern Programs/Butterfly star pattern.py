# wrong answer:
# n=int(input("Enter row number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j or j==n+1-i:
#             print("*", end="")
#         else:
#             print(" ",end="")
#
#     print()

n = int(input("Enter row number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*", end="")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*", end="")
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*", end="")
    print()