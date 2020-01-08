import turtle
screen = turtle.Screen()
trtle1 = turtle.Turtle()
trtle2 = turtle.Turtle()

trtle1.color('Brown')
trtle1.begin_fill()

for _ in range(2):
    trtle1.forward(50)
    trtle1.left(90)
    trtle1.forward(100)
    trtle1.left(90)
trtle1.end_fill()

trtle2.penup()
trtle2.goto(100,100)
trtle2.pendown()
trtle2.setheading(90)
trtle2.color('Green')
trtle2.begin_fill()


for _ in range(2):
    trtle2.left(60)
    trtle2.forward(100)

trtle2.goto(100,100)
trtle2.end_fill()


screen.mainloop()