# list
menu = ["Cơm", "Cá", "Rau muống"]

# separator
# print(*menu, sep=", ")

# lenght
# print(len(menu))
menu.append("Ghẹ")
# print(len(menu))

# for i in range(len(menu)):
#     print(menu[i])

# for index, item in enumerate(menu):
#     print(index + 1, item, sep=".", end=" ")

# for item in menu:
#     print(item)

# for index, item in enumerate(menu):
#     print("{}. {}".format(index + 1, item))

#update
print(*menu, sep=", ")
menu[3] = "Gà"
print(*menu, sep=", ")
