from turtle import *

shape("turtle")
color("blue")
speed(-1)

left(60)
for i in range(2):
    forward(100)
    left(60)
    forward(100)
    left(120)
    forward(100)
    left(60)
    forward(100)
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    left(90)

mainloop()