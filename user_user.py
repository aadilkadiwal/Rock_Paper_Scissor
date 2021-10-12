# Playing Rock, Paper, Scissor with your friend

# Player name
print("Hey Let's play the Rock, Paper, Scissor game")
user1_name = input('Enter Player 1 name : ')
user2_name = input('Enter Player 2 name : ')

# To exit the game
play = True

# Initial Score of user1_name
user1_score = 0

# Initial Score of user2_name
user2_score = 0

# Score card
def score(win):

    # user1 Score card
    if win == 'user1 win':
        global user1_score
        user1_score += 1
    
    # user2 Score card
    elif win == 'user2 win':
        global user2_score
        user2_score += 1    
    
    # Score card status
    print('---------------------')
    print('Current Score Status ')
    print(f'{user1_name.title()} Score : {user1_score}')
    print(f'{user2_name.title()} Score : {user2_score}')
    print('---------------------')

# Who win win user1_name or user2_name
def win_or_loss(user1_name, user2_name, user1, user2):
    print(f'---> {user1_name.title()} Selected : {user1}')
    print(f'---> {user2_name.title()} Selected : {user2}')
    
    # Tie between user1_name and user2_name
    if user1 == user2:
        print('There is a Tie')

    # All possibilities where user1_name win     
    elif (user1 == 's' and user2 == 'p') or (user1 == 'p' and user2 == 'r') or (user1 == 'r' and user2 == 's'):    
        print(f'{user1_name.title()} has win this round')
        return 'user1 win'
   
    # All possibilities where user2_name win
    else:
        print(f'{user2_name.title()} has win this round')
        return 'user2 win'

# Start the game
while play != False:
    print(f'<--- {user1_name.title()} Turn --->')
    user1 = input("Enter 'r' for Rock, Enter 'p' for Paper, Enter 's' for Scissor : ").lower()
    if user1 == 'exit':
        play = False
        break
    print(f'<--- {user2_name.title()} Turn --->')
    user2 = input("Enter 'r' for Rock, Enter 'p' for Paper, Enter 's' for Scissor : ").lower()
    if user2 == 'exit':
        play = False
    win = win_or_loss(user1_name, user2_name, user1, user2)
    result = score(win)
    print("If you want to exit the game type 'exit'")