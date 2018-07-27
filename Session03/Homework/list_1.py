menu = ["T-Shirt", "Sweater"]
lis = True
while lis:
    nh = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    if nh == "C":
        add = input("Enter new item: ")
        menu.append(add)
        print("Our items:",*menu, sep=", ")
    elif nh == "R":
        print("Our items:",*menu, sep=", ")
    elif nh == "U":
        numb = int(input("Update position? "))
        ni = input("New item? ")
        menu[numb -1] = ni
        print("Our items:",*menu, sep=", ")
    elif nh == "D":
        num = int(input("Delete position? "))
        del menu[num - 1]
        print("Our items:",*menu, sep=", ")
    else:
        lis = False
