import turtle as trtl
spider = trtl.Turtle()
spider.speed(0)
spider.pensize(40)
color = ("red")
spider.circle(20) # Create spider body
legs = 8 # Conigure legs
length = 70
spacing = 360 / legs
spider.pensize(5)
n = 0
while (n < legs): # Draw legs
  spider.goto(0,20)
  spider.setheading(spacing*n)
  spider.forward(length)
  n = n + 1
spider.penup()
spider.goto(20, 40)
spider.pendown()
spider.pencolor(color)
spider.circle(10)
spider.penup()
spider.goto(-30, 40)
spider.pendown()
spider.circle(10)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()