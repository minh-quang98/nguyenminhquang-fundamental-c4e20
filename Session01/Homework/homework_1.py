# 1. Sử dụng hàm type()
# 2. Đặt tên biến sau đây thì lỗi
# - Minh Quang (có dấu cách)
# - 1quang (tên có số ở đầu)
# - print (tên trùng hàm có sẵn)

# Rad = int(input("Radius?"))
# area = 3.14 * Rad
# print("Area = ",area)

from turtle import *

shape("turtle")
color("blue","yellow")
speed(-1)
begin_fill()

#A square
# for i in range(4):
#     forward(100)
#     left(90)

#An equilateral triangle
# for i in range(3):
#     forward(150)
#     left(120)

#A circle
# circle(100)
end_fill()

#Multi-circles
for i in range(15):
    circle(100)
    left(30)
mainloop()