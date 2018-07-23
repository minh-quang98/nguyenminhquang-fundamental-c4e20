from turtle import *

shape("turtle")

for j in range(3,7):
    for i in range(j):
        if j == 3 or j == 5:
            color("blue")
        else:
            color("red")
        forward(100)
        left(360/(j))
mainloop()