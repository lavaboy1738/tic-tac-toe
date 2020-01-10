from random import randint
print("\n\n\n")
print("Welcome to Tic Tac Toe")
print('')
print("The current version of the game requires 2 players.\nAI player is not yet available and is currently under development.")
print('')
player_name1 = input("Please enter player 1 name: ")
player_name2 = input("Please enter player 2 name: ")
print("\n")
print ("Hello", player_name1, "and", player_name2+", welcome to Ronnie's first attempt at writing a game.\nI hope you enjoy playing it as much as I did writing it.")
print('\n')
print("Here's the Tic-Tac-Toe Board:")
print('')
board = ["#","1","2","3","4","5","6","7","8","9"]

def display_board(board):
    print('\n'*100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def display_board_first_time(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
display_board_first_time(board)

def player_input():
    player_choice = ''
    
    while not (player_choice == 'X' or player_choice == 'O'):
        player_choice = input('Do you want to be X or O? ').upper()
    if player_choice == 'X':
        return ('X', 'O')
    elif player_choice == "O":
        return ('O', 'X')

def place_player_piece(board, player_choice, position):
    board[position] = player_choice
    

def win_check(board,player_choice):
    #checks all possible combinations
    #check all the rows, then columns, then diagonals
    return ((board[7] == player_choice and board[8] == player_choice and board[9] == player_choice) or 
    (board[4] == player_choice and board[5] == player_choice and board[6] == player_choice) or 
    (board[1] == player_choice and board[2] == player_choice and board[3] == player_choice) or 
    (board[7] == player_choice and board[4] == player_choice and board[1] == player_choice) or 
    (board[8] == player_choice and board[5] == player_choice and board[2] == player_choice) or 
    (board[9] == player_choice and board[6] == player_choice and board[3] == player_choice) or 
    (board[7] == player_choice and board[5] == player_choice and board[3] == player_choice) or 
    (board[9] == player_choice and board[5] == player_choice and board[1] == player_choice)) 


def choose_first():
    if randint(1,2) == 1:
        print("According to random generator, {} goes first.".format(player_name1))
        return player_name1
    else:
        print("According to random generator, {} goes first.".format(player_name2))
        return player_name2


def space_check(board, position):
    
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    #board is full and it's a tie
    return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        print('')
        position = int(input('Choose your next position: (1-9) '))
        
    return position


def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#running the game with a while loop untill player doesn't want to play no more
#break on the replay()

while True:
    theBoard = [' ']*10
    print('')
    turn = choose_first()
    if turn == player_name1:
        player1_piece, player2_piece = player_input()
    if turn == player_name2:
        player2_piece, player1_piece = player_input()
    
    print('')
    play_game = input('Are you ready to play? Enter Yes or No.')
    print('')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False    
    
    while game_on:
        if turn == player_name1:
                # Player1's turn.
                
            display_board(theBoard)
            position = player_choice(theBoard)
            place_player_piece(theBoard, player1_piece, position)
    
            if win_check(theBoard, player1_piece):
                display_board(theBoard)
                print('')
                print('Congratulations! {} have won the game!'.format(player_name1))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('')
                    print('The board is full! The game is a draw!')
                    break
                else:
                    turn = player_name2
    
        else:
            # Player2's turn.
                
            display_board(theBoard)
            position = player_choice(theBoard)
            place_player_piece(theBoard, player2_piece, position)
    
            if win_check(theBoard, player2_piece):
                display_board(theBoard)
                print('{} has won!'.format(player_name2))
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = player_name1
                    
    if not replay():
        print("Thanks for playing.")
        break    