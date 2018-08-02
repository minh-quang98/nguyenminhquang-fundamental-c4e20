numb = int(input("How many B bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))
if time == 0:
    print("After 0 minutes, we would have {} bacterias".format(numb))
elif time % 2 == 0:
    total = numb * 2 ** (time // 2)
    print("After {} minutes, we would have {} bacterias".format(time, total))
else:
    total = numb * 2 ** ((time - 1) // 2)
    print("After {} minutes, we would have {} bacterias".format(time, total))
print()