from turtle import *

shape("turtle")
col = ["red", "blue", "brown", "yellow", "grey"]
speed(-1)

for j in range (5):
    begin_fill()
    color(col[j])
    for i in range(2):
        forward(100)
        left(90)
        forward(150)
        left(90)
    pu()
    forward(100)
    pd()
    end_fill()
mainloop()