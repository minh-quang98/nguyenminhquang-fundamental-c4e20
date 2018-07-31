money = input("Enter your balance: ")
limon = list(money)
i = len(limon)
for j in range(i):
    i -= 3
    if i > 0:
        limon.insert(i,",")
update = ''.join(limon)
print("your update blance: ", update)

