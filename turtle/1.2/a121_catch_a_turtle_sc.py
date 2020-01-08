import turtle, random, time, leaderboard_sc

#670 wide by 580 tall

trtle = turtle.Turtle()
score_writer = turtle.Turtle()
time_keeper = time.time()

time_limit = 30
score = 0

def update_score():
    global score
    score = score + 1
    score_writer.clear()
    score_writer.write(score, font=('Times', 20, 'normal'))

def change_position():
    x = random.randint(-335,335)
    y = random.randint(-290,290)
    trtle.penup()
    trtle.goto(x,y)
    trtle.pendown()


def handle_click(x,y):
    print('Circle clicked at', x, y)
    update_score()
    change_position()

while (time.time() - time_keeper) < time_limit:
    trtle.shape('circle')
    trtle.shapesize(3)

    trtle.onclick(handle_click)
    score_writer.penup()
    score_writer.goto(300,250)
    score_writer.pendown()
else:
    screen = turtle.Screen()
    screen.clear()
    end = turtle.Turtle()
    end.penup()
    end.goto(-167.5,0)
    end.pendown()
    end.write("You Ended With A Score Of:", font=('Times', 30, 'normal'))
    end.penup()
    end.goto(0,-50)
    end.pendown()
    end.write(score, font=('Times', 30, 'normal'))

screen = turtle.Screen()
screen.mainloop()