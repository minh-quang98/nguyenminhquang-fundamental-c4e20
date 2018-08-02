from math import sqrt
total = 1
grow = True
while grow:
    for i in range(6):
        total = ((1 + sqrt(5)) ** (i+1) - (1 - sqrt(5)) ** (i + 1)) // (2 ** (i + 1) * sqrt(5))
        print("Month {}: {} pair(s) of rabbit".format(i, total))
    if i == 5:
        grow = False