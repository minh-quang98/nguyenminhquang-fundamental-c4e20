from random import randint
numb = randint(1,100)
print(numb)
count = 0
guess = True
while guess:
    n = int(input("Guess my number (1 -100): "))
    if n > numb:
        print("too large")
    elif n < numb:
        print("too litte")
    else:
        print("bingo")
        break
    count += 1
    if count == 7:
        print("You lose")
        guess = False