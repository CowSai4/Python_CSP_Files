import turtle
pen = turtle.Turtle()
pen.speed(0)

num_rows = int(input("How many rows do you want?"))
num_cols = int(input("How many columns do you want?"))
grid_length = int(input("how long do you want?"))

row = 0
col = 0
while row < num_rows:
    while col < num_cols:
        pen.penup()
        pen.goto(col * 50,row * -50)

        pen.pendown()
        leg = 0
        while leg < 4:
            pen.forward(grid_length)
            pen.right(90)
            leg += 1
        col +=1
    row += 1
    col = 0


screen = turtle.Screen()
screen.mainloop()