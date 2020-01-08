import turtle, random

screen = turtle.Screen()
trtle = turtle.Turtle()

def move_up():
    trtle.setheading(90)
    trtle.forward(20)

def move_down():
    trtle.setheading(270)
    trtle.forward(20)

def move_right():
    trtle.setheading(0)
    trtle.forward(20)

def move_left():
    trtle.setheading(180)
    trtle.forward(20)

screen.onkeypress(move_up, 'Up')
screen.onkeypress(move_left, 'Left')
screen.onkeypress(move_right, 'Right')
screen.onkeypress(move_down, 'Down')

screen.listen()
screen.mainloop()