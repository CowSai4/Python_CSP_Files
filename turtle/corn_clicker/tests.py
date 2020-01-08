import turtle

player = turtle.Turtle()
dot = turtle.Turtle()
enemy = turtle.Turtle()
screen = turtle.Screen()

screen.addshape('Pos1.gif')
screen.addshape('Pos2.gif')
screen.addshape('Pos3.gif')
screen.addshape('Pos4.gif')

dot.penup()
dot.shape('circle')
player.penup()

enemy.penup()
enemy.hideturtle()

player.shape('Pos1.gif')

def move_up():
    player.setheading(90)
    player.shape('Pos3.gif')
    dot.setheading(90)
    player.forward(10)

def move_right():
    player.setheading(0)
    player.shape('Pos1.gif')
    dot.setheading(0)
    player.forward(10)

def move_left():
    player.setheading(180)
    player.shape('Pos2.gif')
    dot.setheading(180) 
    player.forward(10)

def move_down():
    player.setheading(270)
    player.shape('Pos4.gif')
    dot.setheading(270)
    player.forward(10)


def fire():
    dot.goto(player.pos())
    dot.goto(dot.xcor(),dot.ycor())
    dot.forward(150)
    dot.showturtle()
    dot.pendown()
    dot.color('red')
    dot.forward(100)
    dot.shapesize(2)
    dot.pensize(2)
    dot.color('orange')
    dot.shapesize(4)
    dot.pensize(4)
    dot.color('yellow')
    dot.shapesize(8)
    dot.pensize(8)
    dot.penup()
    dot.hideturtle()
    dot.shapesize(1)
    dot.pensize(0)
    dot.color('black')




screen.onkeypress(move_up,'Up')
screen.onkeypress(move_right,'Right')
screen.onkeypress(move_left,'Left')
screen.onkeypress(move_down,'Down')
screen.onkeypress(fire,'space')

screen.listen()
screen.mainloop()