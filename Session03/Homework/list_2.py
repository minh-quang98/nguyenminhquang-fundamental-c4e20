# 1.
size = [2, 200, 14, 100, 30, 87]
print("Hello my name is Quang and there are my sheep sizes")
print(size)
print()

# 2.
max = 0
for i in range(len(size)):
    if size[i] > max:
        max = size[i]
        maxIndex = i
print("Now my biggest sheep has size", max, "let's shear it")
print()

# 3.
size[maxIndex] = 8
print("After shearing, here is my flock")
print(size)
print()

# 4.
for i in range(len(size)):
    size[i] += 50
print("One muonth passed, now here is my flock")
print(size)