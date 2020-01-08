import turtle

screen = turtle.Screen()
trtle = turtle.Turtle()

screen.addshape('Jeremiah.gif')
trtle.shape('Jeremiah.gif')

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



screen.listen()
screen.mainloop()