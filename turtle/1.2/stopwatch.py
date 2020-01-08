import turtle, time

screen = turtle.Screen()
time = 0

trtle = turtle.Turtle()

start = turtle.Turtle('circle')
start.color('Green')
start.shapesize(2)


stop = turtle.Turtle('circle')
stop.color('yellow')
stop.shapesize(2)
stop.penup()
stop.goto(100,0)
stop.pendown()

reset = turtle.Turtle('circle')
reset.color('red')
reset.shapesize(2)
reset.penup()
reset.goto(-100,0)
reset.pendown()

writer = turtle.Turtle()
writer.penup()
writer.goto(0,-50)
writer.pendown()

start_time = False
timer_running = False

def start_click(x,y):
        global start_time
        if not start_time:
                start_time = True
                screen.ontimer(change_time, 100)

def stop_click(x,y): 
        global start_time
        start_time = False

def reset_click(x,y):
        global start_time, time
        start_time = False
        time = 0

def change_time():
    global time, start_time
    if start_time == True:
        time += .1
        writer.clear()
        writer.write(round(time,1), font=('Times', 20, 'normal'))
        timer_running = True
        screen.ontimer(change_time, 100)


start.onclick(start_click)
stop.onclick(stop_click)
reset.onclick(reset_click)

screen.mainloop()