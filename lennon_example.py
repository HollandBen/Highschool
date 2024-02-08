# Name: Lennon Harford
# Date: 2024-02-04
# Program Details: Example tic tac toe for ben

# used for clearing the terminal
import os

# display_board takes in a list of characters called the board, and the player which is 'x' or 'o'. display_board returns nothing
def display_board(board, player):
    # clears the terminal, says enter 'cls' into command prompt
    os.system("cls")  
    
    # the f and the {} allow us to print off variables inside a string
    print(f"Player: {player}") 
    
    # prints the board
    print(f" {board[0]} | {board[1]} | {board[2]}\t 1 | 2 | 3 ")
    print(f"---+---+---\t---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}\t 4 | 5 | 6 ")
    print(f"---+---+---\t---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}\t 7 | 8 | 9 ")

# get_input takes in the board and the current player and returns an int from 0 - 8 which is the index of the move (0-8 not 1-9 since lists start at index 0)
def get_input(board, player):
    
    # runs the display_board function and provides it with the board and the player
    display_board(board, player)

    try:
        # input() allows us to give a prompt and has it return a string of what the user typed
        # int() converts the "1" (a string) for example into 1 (an integer)
        # if the user types a letter in, python will throw a ValueError, which will be caught by the try-except and the except clause will be run
        # - 1 subtracts the number by 1 since lists start at 0
        index = int(input("Enter move: ")) - 1
        
        # checks if the index is between 0 and 8, and makes sure that the spot they are trying to go is also empty
        if index in [0,1,2,3,4,5,6,7,8] and board[index] == '-':
            # returns the index
            return index
        else:
            # runs get_input again, and whenever a valid index is found, it will return it
            return get_input(board, player)
    # except clause that runs if they type "a" in for example
    except ValueError:
        # runs get_input again, and whenever a valid index is found, it will return it
        return get_input(board, player)

# check_win takes in the board, and will return either the player who won, or None
def check_win(board):
    # win_cases is a list of several lists, each representing indexes in the board that need to be checked for three-in-a-row
    win_cases = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    
    # runs through every case ([0,1,2] for example) in win_cases
    for case in win_cases:
        
        # runs confirm_row (with case and board as arguments) and saves the returned value with the result variable
        result = confirm_row(case, board)
        
        # if the result exists (is not None), then return the result ('x' or 'o' depending on who won)
        if result:
            return result
    # if there are no successful three-in-a-rows, then return None
    return None
            
# confirm_row takes in the case list and the board list and returns either the winner, or None
def confirm_row(case, board):
    # checks if board[0] is equal to board[1] and is equal to board[2] and is not equal to "-". (if case is [0,1,2])
    if board[case[0]] == board[case[1]] == board[case[2]] != "-":
        # returns the winner
        return board[case[0]]
    else:
        # returns None
        return None

def main():
    # current_player is a variable used to store either 'x' or 'o'
    current_player = 'x'
    
    # board is a list which represents all of the spots on the board
    board = ['-','-','-','-','-','-','-','-','-']
    
    # while True will repeat the code indented over and over until 'break' runs
    while True:
        
        # the check_win function is run (with the board as an argument) and the value returned by the function is stored in the variable 'winner'
        winner = check_win(board)
                
        # if a winner exists (is not None), then a print statement will say who won and 'break' will exit the loop and end the program
        if winner:
            print(f"{winner} wins!")
            break
        
        # get_input is run (with board and current_player as arguments) and the index that is returned by the function is stored in the 'index' variable
        index = get_input(board, current_player)
        
        # sets whichever spot on the board where the player typed in, to whichever the current player is
        board[index] = current_player
        
        # runs the display_board function (with board and current_player as arguments)
        display_board(board, current_player)

        # the if-else is responsible for switching the player from 'x' to 'o', or from 'o' to 'x'
        if current_player == 'x':
            current_player = 'o'
        else:
            current_player = 'x'

# the first thing that runs in the program (good coding practice)
if __name__ == "__main__":
    # runs the main function
    main()