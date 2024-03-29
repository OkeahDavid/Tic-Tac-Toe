#Milestone Project 1
#TIC-TAC-TOE Game

from IPython.display import clear_output

def display_board(board):
    clear_output()
    #print('  |','  |')
    print(board[7]+ '|'+board[8]+'|'+board[9])
    print('---------')
    print(board[4]+ '|'+board[5]+'|'+board[6])
    #print('  |','  |')
    print('---------')
    print(board[1]+ '|'+board[2]+'|'+board[3])
    pass
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
    marker=''
    while not (marker=='O' or marker=='X'):
        marker=input("Please choose 'X' or 'O': " ).upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
#player_input()

def place_marker(board, marker, position):
    board[position]=marker
    pass
#place_marker(test_board,'$',8)
#display_board(test_board)


def win_check(board, mark):
    return((board[7]==mark and board[8]==mark and board[9]==mark) or
           (board[4]==mark and board[5]==mark and board[6]==mark) or
           (board[1]==mark and board[2]==mark and board[3]==mark) or
           (board[7]==mark and board[4]==mark and board[1]==mark) or
           (board[8]==mark and board[5]==mark and board[2]==mark) or
           (board[9]==mark and board[6]==mark and board[3]==mark) or
           (board[7]==mark and board[5]==mark and board[3]==mark) or
           (board[9]==mark and board[5]==mark and board[1]==mark)           
           )
    pass
#print(win_check(test_board,'X'))
import random

def choose_first():
    rand=random.randint(0,1)
    if rand==0:
        return "Player 2"
    else:
        return "Player 1"
    pass

def space_check(board, position):
    return board[position] == ' '
    pass

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
    pass

def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board, position):
        position=int(input("input a number from 1-9: "))
    return position
    pass

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
    pass

print('Welcome to Tic Tac Toe!')

while True:
     # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break