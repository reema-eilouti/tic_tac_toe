#Tic-Tac-Toe

#Importing some additional (optional) packages.
import pyfiglet # To draw the group's name
import termcolor # To color some outputs
import datetime # To display current time

# Global variables
#Players Variables
players = () # Tuple to save: ('Player1 Marker', 'Player2 Marker')/('X','O') or ('O','X')
player = '' # One of the tuple's items unpacked (changes every turn from 'X' to 'O' and vice-versa)
player_turn = 1 # Counter from 1 to 9 increments every turn
# Game board
board=[] # The board's 9 spaces stored in a list

def initalize_game():
    """This function initializes the game board spaces with #s then calls the function assign_players()"""

    for b in range(9):
        board.insert(b,'#')    
    
    assign_players()

def display_board(board):
    """This function prints out the game board"""

    print("\n")
    print(f"\t{board[6]}\t|\t{board[7]}\t|\t{board[8]}")
    print(f"\t{board[3]}\t|\t{board[4]}\t|\t{board[5]}")
    print(f"\t{board[0]}\t|\t{board[1]}\t|\t{board[2]}")
    print("\n")    

def place_marker(board, player, position):
    """This function places the player's marker in the desired position on the game board,
    then increments the player_turn and calls the functions display_board() and check_win()"""
    
    board[position] = player

    global player_turn 
    player_turn += 1

    display_board(board)

    check_win(board, player)

def check_space(board, position):
    """This function checks if the space the player chose is empty or not
    if empty it calls the functions place_marker() then player_choice
    if not empty it prompts the user to chose another and calls player_choice()"""

    if board[position] == '#':
        place_marker(board, player, position)
        player_choice(player, board)
    else:
        print("The space you chose is already used!")
        player_choice(player, board)
        
def player_choice(player, board):
    """This function asks the user to choose a space on the board to play on
    it checks the input, if valid it calls check_space()
    if not valid it prompts the user and calls itself"""
      
    space = int(input("Please choose a space from 0-8: "))
    
    if space in range(9):
        check_space(board, space)
    else:
        print("You didn't choose a valid space!")
        player_choice(player, board)

def assign_players():
    """This function asks the user to pick a marker 'X' or 'O',
    if the input is valid it assigns the markers to the global variable players then calls check_board_full()
    if the input is not valid it prompts the user then calls itself"""

    global players

    player1 = input("\nPlease pick a marker 'X' or 'O': ").upper()
    
    if player1 == 'X':
        player2 = 'O'
        players = (player1, player2)
        check_board_full(board)
    elif player1 == 'O':
        player2 = 'X'
        players = (player1, player2) 
        check_board_full(board)            
    else:
        print("You didn't enter a valid marker!")
        assign_players()

def check_board_full(board):
    """This function counts the number of spaces left empty on the game board
    if the user reaches this point in the game with no more empty spaces then it's a draw and replay() is called
    if there is one or more empty spaces the function sets the right marker to the global variable player"""
    
    count = 0
    for space in board:
        if space == '#':
            count += 1            
                       
    if count >= 1: 
        if player_turn % 2 == 0:
            global player 
            player = players[1]
            player_choice(player, board)
        else:
            player = players[0]
            player_choice(player, board)
    else:
        print(termcolor.colored("Oh, it's a Draw -_-", color="blue"))
        replay()
    
def check_win(board, mark):
    """This function checks if there is a win on the board
    if yes it calls replay() if no it calls check_board_full()"""

    # Checking rows for a win    
    if (board[0] == board[1] == board[2] == mark) or (board[3] == board[4] == board[5] == mark) or (board[6] == board[7] == board[8] == mark):
        print(termcolor.colored(f"player {player} won!", color='green'))        
        replay()
    # Checking coloumns for a win
    if (board[0] == board[3] == board[6] == mark) or (board[1] == board[4] == board[7] == mark) or (board[5] == board[2] == board[8] == mark):
        print(termcolor.colored (f"player {player} won!" , color='green'))
        replay()
    # Checking diagonals for a win
    if (board[0] == board[4] == board[8] == mark) or (board[2] == board[4] == board[6] == mark): 
        print(termcolor.colored (f"player {player} won!" , color='green'))
        replay()
    check_board_full(board)
       
def replay():
    """This function asks if the user wishes to start a new game
    if yes it calls initialize_game(), if no it quits the program"""
       
    yes_no=str(input("Do you want to play again? Y/N ").upper())
    if yes_no == "Y":
        initalize_game()
    elif yes_no == "N":
        quit()
    
if __name__ == "__main__":

    print((pyfiglet.figlet_format("Group_3")))

    print(termcolor.colored('\nWelcome to Tic-Tac-Toe!', color='yellow'))

    date_time = datetime.datetime.now()
    day = date_time.strftime("%A")
    print (termcolor.colored (f"Date now is {date_time} - {day}", color='magenta'))
 
    initalize_game()
