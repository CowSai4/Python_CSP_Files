import turtle

screen = turtle.Screen()
trtle = turtle.Turtle()

pen = True

def pen():
    global pen
    if pen == False:
        pen = True
        trtle.pendown()
    else:
        pen = False
        trtle.penup()


def left():
    trtle.setheading(180)
    trtle.forward(10)
    left()

def right():
    trtle.setheading(0)
    trtle.forward(10)
    right()

def up():
    trtle.setheading(90)
    trtle.forward(10)
    up()


def down():
    trtle.setheading(270)
    trtle.forward(10)
    down()


screen.onkeypress(up, 'Up')
screen.onkeypress(left, 'Left')
screen.onkeypress(right, 'Right')
screen.onkeypress(down, 'Down')
screen.onkeypress(pen,'space')


screen.listen()
screen.mainloop()