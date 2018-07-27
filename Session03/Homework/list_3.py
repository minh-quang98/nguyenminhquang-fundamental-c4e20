# 4.
size = [2, 200, 14, 100, 30, 87]
print("Hello my name is Quang and there are my sheep sizes")
print(size)
print()

for i in range(4):
    print("Month", i + 1)
    for i in range(len(size)):
        size[i] += 50
    print("One muonth passed, now here is my flock")
    print(size)
    max = 0
    for i in range(len(size)):
        if size[i] > max:
            max = size[i]
            maxIndex = i
    print("Now my biggest sheep has size", max, "let's shear it")
    size[maxIndex] = 8
    print("After shearing, here is my flock")
    print(size)
    print()

# 5.
total = sum(size)
money = total * 2
print("My flock has size in total: ", total)
print("I would get ", total, "* 2$ =", money,"$")