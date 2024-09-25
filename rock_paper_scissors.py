import random
from colorama import Fore, Back, Style

while True:
    rock = 'Rock'
    paper = 'Paper'
    scissors = 'Scissors'
    computer_move = ''
    points = 0

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        points += 3
        print(Fore.GREEN, Back.BLACK + f'You win! You have {points} points.')
    elif player_move == computer_move:
        points += 1
        print(Fore.YELLOW, Back.BLACK + f'Draw! You have {points} points.')
    else:
        print(Fore.RED, Back.BLACK + f'You lose! You have {points} points.')

    a = input('Type [yes] to play again or [no] to quit: ')
    while a != 'yes' or a != 'no':
        if a == 'yes':
            break
        elif a == 'no':
            print('Thank you for playing!')
            exit()
        else:
            print('Incorrect answer!')
            a = input('Try again!\nType [yes] to play again or [no] to quit: ')


