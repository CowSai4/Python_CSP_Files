import turtle
screen = turtle.Screen()
trtle = turtle.Turtle()

x = 10

for _ in range(5):
    trtle.circle(x)
    x += 10


screen.mainloop()