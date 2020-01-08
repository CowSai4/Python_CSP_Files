import turtle

turtle_list = []
length_list = []


decision = 'yes'

while decision == 'yes':
    color = input('Enter a color: ')
    heading = int(input('Enter a heading: '))
    length = int(input('Enter a length: '))

    current_turtle = turtle.Turtle()
    current_turtle.color(color)
    current_turtle.setheading(heading)


    turtle_list.append(current_turtle)
    length_list.append(length)

    decision = input('Would you like to enter another turtle?')
#for element in iterable
for index in range(len(turtle_list)):
    turtle_list[index].forward(length(length_list))

screen = turtle.Screen()
screen.mainloop()