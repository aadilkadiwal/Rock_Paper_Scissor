# Playing Rock, Paper, Scissor game with Computer

import random

# List of Rock, Ppaer, and Sissor
game_list = ['s','p','r']

# User input by defult blank
user = ''

# User Score
user_score = 0

# Computer Score
comp_score = 0

# Score Status
def score(win_loss):

    # User Score card
    if win_loss == 'user win':
        global user_score
        user_score += 1 
    
    # Computer Score card
    elif win_loss == 'comp win':
        global comp_score
        comp_score += 1
    
    # Score card Status
    print('--------------------------')
    print('Current Score Status ')
    print(f'Computer Score : {comp_score}')
    print(f'{user_name.title()} Score : {user_score}')
    print('--------------------------')      

# Computer play
def computer():
    r_p_s = random.choice(game_list)
    return r_p_s

# Win or Loss
def win_or_loss(user, comp):

    # Tie between User and Computer
    if comp == user:
        print('Well! There is a Tie')

    # All possibilities where Computer win    
    elif (comp == 's' and user == 'p') or (comp == 'p' and user == 'r') or (comp == 'r' and user == 's'):
        print('Oops! Computer win this Round')
        return 'comp win'

    # Possibilities where User win    
    else:
        print(f'Awesome! {user_name.title()} win this Round')
        return 'user win'

# Player name
user_name = input('Enter Your name : ')
print(f'Hey! {user_name.title()} Lets Play the Game')

# Start the game
while user != 'exit':
    user = input("Enter 's' for Scissor, Enter 'p' for Paper, Enter 'r' for Rock : ").lower()
    comp = computer()
    print(f'Computer Select : {comp}')
    win_loss = win_or_loss(user, comp)
    result = score(win_loss)
    print("If you want to exit game type 'exit'")
