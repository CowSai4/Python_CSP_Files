import turtle


trtle = turtle.Turtle()

color = input("Give me any color:  ")
print(color)
number = int(input("Give me the length:  "))
print(number)
sides = int(input("How many sides?"))
print(sides)

trtle.color(color)

angle = 360/sides
x = 0
while( x < sides):
    trtle.forward(number)
    trtle.right(angle)
    x = x+1


screen = turtle.Screen()
screen.mainloop()