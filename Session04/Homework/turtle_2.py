from turtle import *

shape("turtle")
color("blue")
speed(-1)

for j in range(42):
    for i in range(4):
        forward(j*3)
        left(90)
    left(12)

mainloop()