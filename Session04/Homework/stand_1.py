name = input("Enter your name: ").lower()
linam = name.split()
for i in range(len(linam)):
    linam[i] = linam[i].capitalize()
print("Update: ", *linam)