number = int(input("Enter number: "))
# count = 0
# for i in range(1, (number + 1)**0.5:
#     number % i == 0
#     count +=1
# if count == 2:
#     print("It's prime number")
# else:
#     print("It is'n prime number")
    

is_prime = True
i = 2
while i < number**0.5:
    if number % i == 0:
        is_prime = False
    i += 1
if is_prime:
    print("{} is a prime number".format(number))
else:
    print("{} is not a prime number".format(number))
