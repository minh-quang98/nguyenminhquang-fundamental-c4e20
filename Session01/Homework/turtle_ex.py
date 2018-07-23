from turtle import * 

shape("turtle")
color("red","cyan")
speed(-1)
begin_fill()
for i in range(100):
    for i in range(4):
        forward(100)
        left(90)
    right(7)

# n = int(input("Nhập số cạnh"))
# for i in range(n):
#     forward(50)
#     left(360/n)
# print(n)
end_fill()
mainloop()