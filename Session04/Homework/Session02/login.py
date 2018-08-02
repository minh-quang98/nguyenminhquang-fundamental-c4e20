import getpass
Name = input("Username = ")
if Name == "c4e":
    Pas = getpass.getpass('Password = ')
    if Pas == "ctc":
        print("Welcome, c4e")
    else:
        print("incorrecr password")
else:
    print("login fail")