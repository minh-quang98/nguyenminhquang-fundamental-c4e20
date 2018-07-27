from turtle import *

shape("turtle")
col = ["red", "blue", "brown", "yellow", "grey"]
speed(-1)

for i in range(3,len(col)+3):
    color(col[i-3])
    for j in range(i):
        forward(100)
        left(360/i)
mainloop()