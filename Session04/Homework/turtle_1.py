from turtle import *

shape("turtle")
color("blue")
speed(-1)

for j in range(24):
    for i in range(4):
        forward(100)
        left(90)
    left(15)

mainloop()