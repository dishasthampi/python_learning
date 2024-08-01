# n = int(input("Enter number of rows"))
# for i in range(1, n+1):
#     for j in range(n, 0, -1):
#         if j <= i:
#             print(i, end=" ")
#         else:
#             print("", end=" ")
#     print()


n = int(input("Enter number of rows"))
for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ", end = "")
    for j in range(1,i+1):
        print(i, end =" ")
    print()



