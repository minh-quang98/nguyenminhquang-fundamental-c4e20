print("Think one number from (0 - 100), then press 'Enter")
input()
print("""
All you have to do is to answer to my guess
'c' if 'C'orrect
'l' if 'L'arge
's' if 'S'mall
""")
low = 0
high = 100
guess = True

while guess:
    mid = (low + high) // 2
    ask = input("Is {} your number?".format(mid))
    if ask == "s":
        low = mid
    elif ask == "l":
        high = mid
    elif ask == "c":
        print("Yay!!")
        guess = False
    else:
        break


# playing =True
# while playing:
#     mid =(low + high)//2

#     guess = input("Is {} your number: ".format(mid))

#     if guess == "c":
#         print("yay!!")
#         playing = False
#     elif guess == "s":
#         low = mid
#     elif guess == "l":
#         high = mid





