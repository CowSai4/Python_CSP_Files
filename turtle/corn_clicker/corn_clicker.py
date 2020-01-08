import turtle, random, sys, time
from multiprocessing import Process

time = 0
sec = 0

has_clicked = False

screen = turtle.Screen()
corn = turtle.Turtle()
corn2 = turtle.Turtle()
corn_dog = turtle.Turtle()
screen.addshape('corn.gif')
screen.addshape('popcorn.gif')
screen.addshape('corn_dog.gif')
screen.addshape('corn2.gif')
corn.shape('corn.gif')
corn2.shape('corn2.gif')
corn_dog.shape('corn_dog.gif')

corn2.hideturtle()
corn_dog.hideturtle()

corn_dog.penup()
corn2.penup()
corn.penup()



upgrade_writer = turtle.Turtle()
upgrade_writer.hideturtle()
upgrade_writer.penup()
upgrade_writer.goto(25,100)
upgrade_writer.pendown()

corn_writer = turtle.Turtle()
corn_writer.hideturtle()
corn_writer.penup()
corn_writer.goto(-150,100)
corn_writer.pendown()

corn_multiplier = 1
corn_total = 0
popcorn_list = []
upgrade_list = []

class Popcorn:
    def __init__(self):
        popcorn_trtl = turtle.Turtle()
        popcorn_trtl.shape('popcorn.gif')
        popcorn_trtl.penup()
        popcorn_trtl.hideturtle()
        popcorn_trtl.speed(0)
        popcorn_list.append(popcorn_trtl)
        popcorn_trtl.goto(random.randint(-188, 188), random.randint(-92, 92))
        popcorn_trtl.showturtle()

def purchase_autoclick():
    global corn_total
    if corn_total >= 25:
        if 'autoclick' not in upgrade_list:
            corn_total += -25
            update_counter()
            upgrade_list.append('autoclick')
            upgrade_writer.clear()

def purchase_multiplier():
    global corn_total, corn_multiplier
    if corn_total >= 50:
        if 'multiplier' not in upgrade_list:
            corn_total += -50
            update_counter()
            upgrade_list.append('multiplier')
            upgrade_writer.clear()
            corn_multiplier *= 2

def display_upgrade_unlocks():
    if corn_total == 25:
        if 'auto_clicker' not in upgrade_list:
            upgrade_writer.clear()
            upgrade_writer.write('Autoclicker unlocked. Press 1 to purchase with 25 corn', font=('Times New Roman', 20, 'normal'))
    if corn_total == 50:
        if 'corn_multiplier' not in upgrade_list:
            upgrade_writer.clear()
            upgrade_writer.write('Multiplier unlocked. Press 2 to purchase with 50 corn', font=('Times New Roman', 20, 'normal'))

def corn_clicked(x, y):
    global corn_total, has_clicked
    if not has_clicked:
        has_clicked = True
        corn_total += 1 * corn_multiplier
        if len(popcorn_list) <= 5:
            popcorn_trtl = Popcorn()
        update_counter()
        upgrade_writer.clear()
        has_clicked = False

def update_counter():
    corn_writer.clear()
    message = 'Corn: ' + str(corn_total)
    corn_writer.write(message, font=('Times New Roman', 20, 'normal'))

def change_time():
    global sec, time
    screen.ontimer(change_time, 100)
    time += 1
    move_trtls()
    display_upgrade_unlocks()

    if float(time % 10) == float(0):
        sec += 1
        if float(sec % 5) == float(0):
            if 'autoclick' in upgrade_list:
                auto_clicker()

def move_trtls():
    for popcorn_trtl in popcorn_list:
        popcorn_trtl.goto(popcorn_trtl.xcor(), popcorn_trtl.ycor() - 25)
        if popcorn_trtl.ycor() <= -500:
            popcorn_list.remove(popcorn_trtl)
            popcorn_trtl.hideturtle()

def auto_clicker():
    corn_clicked(0, 0)

def dog():
    corn.hideturtle()
    corn2.hideturtle()
    corn_dog.showturtle()

def corn_2():
    corn.hideturtle()
    corn_dog.hideturtle()
    corn2.showturtle()

def normal_corn():
    corn2.hideturtle()
    corn_dog.hideturtle()
    corn.showturtle()

change_time()
corn.onclick(corn_clicked)
screen.onkeypress(purchase_autoclick,'1')
screen.onkeypress(purchase_multiplier, '2')
screen.onkeypress(dog,'Up')
screen.onkeypress(corn_2,'Down')
screen.onkeypress(normal_corn,'Left')
corn_dog.onclick(corn_clicked)
corn2.onclick(corn_clicked)

screen.listen()
screen.mainloop()