# print("Hello, here is your favorite")
menu = ["Reading", "LOL", "Facebook"]
# print(*menu, sep=", ")
# add = input("Add your favor: ")
# menu.append(add)
# print(*menu, sep=", ")
for i in range(30):
    print("*", end="")
print()

for index, item in enumerate(menu):
    print("{}. {}".format(index +1, item))

for i in range(30):
    print("*", end="")
print()

numb = int(input("Position you want replace: "))
favor = input("Your favor replace: ")
menu[numb - 1] = favor

for i in range(30):
    print("*", end="")
print()

for index, item in enumerate(menu):
    print("{}. {}".format(index +1, item))

for i in range(30):
    print("*", end="")
