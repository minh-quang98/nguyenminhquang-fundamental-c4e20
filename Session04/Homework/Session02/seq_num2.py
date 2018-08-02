# for i in range(16):
#     print("1 ", end="0 ")

n = int(input("Nhập tổng số 1 và số 0: "))
for i in range(n):
    if i % 2 == 1:
        print("0", end=" ")
    else:
        print("1", end=" ")