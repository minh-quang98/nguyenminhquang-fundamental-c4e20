from random import *

string = ["CHAMPION", "HERO", "SCHOOL", "SHOOT"]
string = choice(string)
work = list(string)

updated_work = []
loop = True
while loop:
    rand_work = choice(work)
    updated_work.append(rand_work)
    work.remove(rand_work)
    if len(work) == 0:
        loop = False

print(*updated_work)
ans = input("Guess work:").upper()
if ans == string:
    print("Correct")
else:
    print("Wrong")
