import turtle
screen = turtle.Screen()

#Go to Desmos and sign in with school email to plot points
scene = input("Tell me something and i'll show you how I feel about it: ")


def stuff():
    global scene

    print(scene)

    body = turtle.Turtle()
    arms = turtle.Turtle()
    head = turtle.Turtle()
    hands = turtle.Turtle()
    text = turtle.Turtle()

    body.speed(0)
    arms.speed(0)
    head.speed(0)
    hands.speed(0)
    text.speed(0)

            #you were using 'or' the wrong way, you have to do something like "if scene == 'hw' or scene == 'history' etc..."
            #the easiest way to do what you were trying to do is what i did below

    if scene in ['hw', 'history', 'english', 'business']:
        # Scene 1

        # Text 1
        text.penup()
        text.goto(150,0)
        text.pendown()
        text.write(scene, font=("Times New Roman", 20, "normal"))

        # Body 1
        body.penup()
        body.goto(-58,-65)
        body.pendown()
        body.goto(55,-65)
        body.goto(67,10)
        body.goto(50,85)
        body.goto(-20,100)
        body.goto(-78,80)
        body.goto(-44,10)
        body.goto(-58,-65)

        # Arms 1 / left arm
        arms.penup()
        arms.goto(-78,80)
        arms.pendown()
        arms.goto(-113,23)
        arms.goto(-92.5,2.5)
        arms.goto(-15.5,25)
        arms.goto(-24,46.6)
        arms.goto(-57.5,39)
        arms.goto(-54,72)
        arms.goto(-57.5,39)
        arms.goto(-88.6,31)

        # Arms 1 / right arm
        arms.penup()
        arms.goto(50,85)
        arms.pendown()
        arms.goto(69,83)
        arms.goto(90.5,21)
        arms.goto(74,-47)
        arms.goto(48,-38)
        arms.goto(64,20)
        arms.goto(33,79)
        arms.goto(50,85)

        # Hands 1 / left hand
        hands.penup()
        hands.goto(-32,25)
        hands.pendown()
        hands.goto(-10,25)
        hands.goto(-6.5,40)
        hands.goto(0,48)
        hands.goto(5,45)
        hands.goto(-10,25)
        hands.goto(-2,65.5)
        hands.goto(-24,62.5)
        hands.goto(-32,25)

        # Hands 1 / right hand
        hands.penup()
        hands.goto(74,-47)
        hands.pendown()
        hands.goto(58,-62)
        hands.goto(39,-49.8)
        hands.goto(48,-38)
        hands.goto(39.2,-40)
        hands.goto(43.4,-43.4)

        # Head 1 
        head.penup()
        head.goto(-28,88.5)
        head.pendown()
        head.circle(45)
        head.penup()
        head.goto(-42.7,103.35)
        head.pendown()
        head.goto(-33,112.3)
        head.goto(-15.5,108.5)
        head.penup()
        head.goto(-12,134)
        head.pendown()
        head.right(160)
        head.forward(15)
        head.penup()
        head.forward(20)
        head.pendown()
        head.forward(15)

        body.penup()
        arms.penup()
        head.penup()
        hands.penup()
        text.penup()

        body.goto(1000000,0)
        arms.goto(1000000,0)
        head.goto(1000000,0)
        hands.goto(1000000,0)
        text.goto(1000000,0)
    elif scene in ['csp', 'engineering', 'physics', 'math', 'video games']:
        # Scene 2
        
        # Text 2 
        text.penup()
        text.goto(150,0)
        text.pendown()
        text.write(scene, font=("Times New Roman", 20, "normal"))

        # Body 2
        body.penup()
        body.goto(-82.4,-67.7)
        body.pendown()
        body.goto(26.3,-67.7)
        body.goto(46.6,64.2)
        body.goto(-2.5,78)
        body.goto(-62,64.5)
        body.goto(-82.4,-67.7)

        # Arms 2 / left arm
        arms.penup()
        arms.goto(-62,64.5)
        arms.pendown()
        arms.goto(-82.05,70)
        arms.goto(-106,13)
        arms.goto(-116.5,-51.5)
        arms.goto(-100.5,-55.5)
        arms.goto(-71.2,4.5)

        # Arms 2 / right arm
        arms.penup()
        arms.goto(46.6,64.2)
        arms.pendown()
        arms.goto(64,66)
        arms.goto(98.7,-39.8)
        arms.goto(99.85,-51.95)
        arms.goto(66,-57.8)
        arms.goto(35.1,-11)
        arms.goto(52.8,-8.8)
        arms.goto(98.7,-39.8)
        arms.penup()
        arms.goto(44.85,21.7)
        arms.pendown()
        arms.goto(41.6,30.8)

        # Head 2
        head.penup()
        head.goto(-46,68.5)
        head.pendown()
        head.goto(-32.5,89)
        head.penup()
        head.goto(30.5,69)
        head.pendown()
        head.goto(16.2,87.6)
        head.penup()
        head.goto(-13.4,112.2)
        head.pendown()
        head.left(150)
        head.forward(10)
        head.back(10)
        head.right(90)
        head.forward(10)
        head.right(60)
        head.penup()
        head.goto(0,131.25)
        head.pendown()
        head.back(10)
        head.penup()
        head.back(10)
        head.pendown()
        head.back(10)
        head.penup()
        head.goto(-7.3,78)
        head.pendown()
        head.circle(35)

        # Hands 2 / left hand
        hands.penup()
        hands.goto(-116.5,-51.5)
        hands.pendown()
        hands.goto(-124,-57)
        hands.goto(-123,-61.2)
        hands.goto(-110.5,-67.7)
        hands.goto(-98.5,-62)
        hands.goto(-100.5,-55.5)
        hands.goto(-110.5,-67.7)
        hands.penup()
        hands.goto(-100.5,-55.5)
        hands.pendown
        hands.goto(-116.5,-51.5)

        # Hands 2 / right hand
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.circle(15,45)
        hands.pendown()
        hands.goto(40,-5.75)
        hands.goto(38.25,-2.5)
        hands.goto(47,-1.5)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(45)
        hands.circle(17,90)
        hands.pendown()
        hands.goto(47,-1.5)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(90)
        hands.circle(17,90)
        hands.pendown()
        hands.goto(32.5,-0.5)
        hands.goto(30.8,3)
        hands.goto(41.3,7.15)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(90)
        hands.circle(17,112.5)
        hands.pendown()
        hands.goto(41.3,7.15)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(112.5)
        hands.circle(17,112.5)
        hands.pendown()
        hands.goto(38.7,12.6)
        hands.goto(27.8,7.1)
        hands.goto(27.25,10.25)
        hands.goto(37,17.5)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(112.5)
        hands.circle(17,135)
        hands.pendown()
        hands.goto(37,17.5)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(135)
        hands.circle(17,135)
        hands.pendown()
        hands.goto(67.65,34)
        hands.goto(66.5,38.6)
        hands.goto(57.7,29.9)
        hands.goto(44.85,21.7)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(135)
        hands.circle(17,180)
        hands.pendown()
        hands.goto(27.75,27.5)
        hands.goto(22.5,25.5)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(180)
        hands.circle(17,215)
        hands.pendown()
        hands.goto(22.5,25.5)
        hands.penup()
        hands.goto(40.5,-12.2)
        hands.right(215)
        hands.pendown()
        hands.circle(17,360)

        body.penup()
        arms.penup()
        head.penup()
        hands.penup()
        text.penup()

        body.goto(1000000,0)
        arms.goto(1000000,0)
        head.goto(1000000,0)
        hands.goto(1000000,0)
        text.goto(1000000,0)

stuff()

times = int(input('How much do you want to tell me? '))
x = 0

while x < times:
    scene = input('Tell me more:    ')
    screen.clear()
    stuff()
    x = x + 1

screen.mainloop()