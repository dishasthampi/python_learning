# n= int(input("Enter row number"))
# for i in range(1, n+1):
#     for j in range(1, n+2-i):
#         print(j,end=" ")
#     print()

n = int(input("Enter row number"))
for i in range(1, n+1):
    for j in range(1,n-i+2):
        print(j,end=" ")
    print()

