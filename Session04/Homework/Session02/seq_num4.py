# for j in range(5):
#     for i in range(5):
#         if i % 2 == 1:
#             print("0 ", end="")
#         else:
#             print("1 ", end="")
#     print()


n = int(input("Enter number: "))
for i in range(n):
    for j in range(n):
        if j % 2 ==1:
            print("0 ", end="")
        else:
            print("1 ", end="")
    print()