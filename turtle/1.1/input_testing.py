import turtle


trtle = turtle.Turtle()

color = input("Give me any color:  ")
print(color)
number = int(input("Give me the length:  "))
print(number)

trtle.color(color)
trtle.right(90)
trtle.forward(number)


screen = turtle.Screen()
screen.mainloop()