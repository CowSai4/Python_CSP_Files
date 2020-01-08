import turtle, random

screen = turtle.Screen()

writer = turtle.Turtle()
screen.addshape('Jeremiah.gif')

'''j_list = []

def create(x,y):
    j = turtle.Turtle('Jeremiah.gif',visible=False)
    j.penup()
    j.goto(x,y)
    j.showturtle()
    j_list.append(j)
    print(len(j_list))

for j in j_list:
    j.pendown()
    j.write('Ooga Booga',font=('Comic Sans',100,'normal'))

screen.onclick(create)'''
x = 0
y = 0
_list = []

ins = input('yummy yummy:   ')

def typer():
    new_x = random.randint(-300,300)
    new_y = random.randint(-300,300)
    writer.goto(new_x,new_y)
    writer.write(ins, font=('Times', 20, 'normal'))

for letter in 'qwertyuiopasdfghjklzxcvbnm':
    screen.onkeypress(typer,'space')


screen.listen()
screen.mainloop()