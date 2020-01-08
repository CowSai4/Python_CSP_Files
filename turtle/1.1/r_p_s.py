import random

print('Welcome to rock, paper, and scissors')
print('Your answer must have the first letter be uppercase')

player_choice = input('Rock, Paper, or Scissors?')
computer_choice = random.choice(['Rock','Paper','Scissors'])
if player_choice == 'Rock' and computer_choice == 'Paper':
    print("You lost!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Rock' and computer_choice == 'Scissors':
    print("You Won!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Rock' and computer_choice == 'Rock':
    print("It's at tie!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Paper' and computer_choice == 'Rock':
    print("You Won!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Paper' and computer_choice == 'Scissors':
    print("You lost!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Scissors' and computer_choice == 'Rock':
    print("You lost!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Scissors' and computer_choice == 'Paper':
    print("You Won!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Paper' and computer_choice == 'Paper':
    print("It's at tie!")
    print('Your choice',player_choice, 'vs',computer_choice)
elif player_choice == 'Scissors' and computer_choice == 'Scissors':
    print("It's at tie!")
    print('Your choice',player_choice, 'vs',computer_choice)
play_again = input('Do you want to play again?')
if play_again == 'yes':
    rounds = int(input('How many rounds do you want to play?'))
    rounds = rounds + 1
    rounds = rounds / 2
    x = 0 
    while(x < rounds):
        player_choice = input('Rock, Paper, or Scissors?')
        computer_choice = random.choice(['Rock','Paper','Scissors'])
        if player_choice == 'Rock' and computer_choice == 'Paper':
            print("You lost!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Rock' and computer_choice == 'Scissors':
            print("You Won!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Rock' and computer_choice == 'Rock':
            print("It's at tie!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Paper' and computer_choice == 'Rock':
            print("You Won!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Paper' and computer_choice == 'Scissors':
            print("You lost!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Scissors' and computer_choice == 'Rock':
            print("You lost!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Scissors' and computer_choice == 'Paper':
            print("You Won!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Paper' and computer_choice == 'Paper':
            print("It's at tie!")
            print('Your choice',player_choice, 'vs',computer_choice)
        elif player_choice == 'Scissors' and computer_choice == 'Scissors':
            print("It's at tie!")
            print('Your choice',player_choice, 'vs',computer_choice)
        x += 1

