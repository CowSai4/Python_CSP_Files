import turtle
trtl = turtle.Turtle()


def draw_square(x,y,size):
    trtl.penup()
    trtl.goto(x,y)
    trtl.setheading(0)
    trtl.pendown()
    for _ in range(4):
        trtl.forward(size)
        trtl.right(90)

draw_square(1,1,100)


screen = turtle.Screen()
screen.mainloop()