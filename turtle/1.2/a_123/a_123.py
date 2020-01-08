import turtle, random
screen = turtle.Screen()


screen.addshape('apple.gif')


screen.bgpic('background.gif')

letters = 'qwertyuiopasdfghjklzxcvbnm'
letter_list = list(letters)

turtle_list = []

current_letters = []

def drop_apple(apple):
    apple.setpos(apple.xcor(), -200)
    apple.hideturtle()
    apple.clear()
    reset_apple(apple)

def reset_apple(apple):
    if len(letter_list) > 0:
        apple.showturtle()
        apple.speed(0)
        new_x = random.randint(-180, 180)
        new_y = random.randint(-45,150 )
        apple.setpos(new_x, new_y)
        apple.speed(5)
        random_letter(apple)
        turtle_list.append(apple)


def random_letter(apple):
    letter = random.choice(letter_list)
    apple.write(letter, font=('Times New Roman',40, 'normal'))
    print(letter)
    letter_list.remove(letter)
    current_letters.append(letter)
    if letter_list == []:
        apple.hideturtle()

def handle_key_press(key):
    if key in current_letters:
        index = current_letters.index(key)
        current_letters.pop(index)
        drop_apple(turtle_list.pop(index))
    

screen.onkeypress(drop_apple, 'space')
screen.listen()

for letter in 'qwertyuiopasdfghjklzxcvbnm':
    screen.onkeypress(lambda l = letter: handle_key_press(l),letter)

for _ in range(5):
    t = turtle.Turtle('apple.gif')
    t.penup()
    reset_apple(t)
    

screen.mainloop()