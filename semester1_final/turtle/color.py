import turtle
screen = turtle.Screen()
trtle = turtle.Turtle()

trtle.shape('circle')
trtle.shapesize(10)

def red():
    trtle.color('red')

def blue():
    trtle.color('blue')

def green():
    trtle.color('green')

def black():
    trtle.color('black')

screen.onkeypress(red,'r')
screen.onkeypress(blue,'b')
screen.onkeypress(green,'g')
screen.onkeypress(black,'q')

screen.mainloop()