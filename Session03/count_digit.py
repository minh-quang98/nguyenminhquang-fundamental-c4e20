count = 0
numb = int(input("Enter a number: "))
while numb > 0:
    numb //= 10
    count += 1
print(count)