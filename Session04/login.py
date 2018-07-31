count = 0
loop = True
while loop:
    if count < 3:
        Name = input("Username = ") 
        if Name == "c4e":
            Pas = input('Password = ')
            if Pas == "ctc":
                print("Welcome, c4e")
                loop = False
            else:
                print("incorrecr password")
                count += 1
        else:
            print("login fail")
            count += 1 
    else:
        print("You false lo log in 3 time, get out of here!!!")
        loop = False
