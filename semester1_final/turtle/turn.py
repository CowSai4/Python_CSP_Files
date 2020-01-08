import turtle
screen = turtle.Screen()
trtle = turtle.Turtle()

trtle.shape('turtle')
trtle.shapesize(10)

z = 0

def turn_360(x,y):
    global z
    while z < 360:
        trtle.setheading(z)
        z += 1
    z = 0

trtle.onclick(turn_360)

screen.mainloop()