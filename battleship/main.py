#Written by Ben Holland
#Date: 6 Feb 2024
#Battleship project

#to do:
#print the updated grid after firing
#make the program run in order correctly
#establish what happens when the win condition is triggered and lose condition



#importations
import random


#starting message and prompt to play the game
start_game = False
def starting_message():
    start_game = False
    while start_game == False:
        print("Welcome to Battleship! \nYou are an elite commander tasked with sinking the two enemy ships that are hiding somewhere in the ocean. Every turn, submit coordinates to send an artillery shot towards the enemy. However, the allied supply lines were cut, and you only have 15 artillery shots to sink the enemy. \nIf your shot hits an enemy battleship, an 'x' will appear, but if you miss, an 'o' will appear.")
        startup = input("Press 1 to start the game: ")
        if startup.isdigit(): #will check to make sure the player did a proper integer input
            commence = int(startup)
            if commence == 1:
                start_game = True
                break

#determine the x and y coordinates of the ship starters
while True:
    x_value_1 = random.randint(0,4)
    y_value_1 = random.randint(0,4)
    ship_direction_1 = random.randint(0,1) #0 is south, 1 is east
    ship_head_1 = [x_value_1, y_value_1]
    if ship_direction_1 == 1 and x_value_1 < 4: # if east ship and not on right border, create tail
        ship_tail_1 = [x_value_1 +1, y_value_1]
        break
    if ship_direction_1 == 0 and y_value_1 < 4: # if south ship and not on bottom border, create tail
        ship_tail_1 = [x_value_1, y_value_1 +1]
        break
        #above and below currently have errors, it can spawn on border still
    
while True:
    while True:
        x_value_2 = random.randint(0,4)
        y_value_2 = random.randint(0,4)
        ship_direction_2 = random.randint(0,1) #0 is south, 1 is east
        ship_head_2 = [x_value_2, y_value_2]
        if ship_direction_2 == 1 and x_value_2 < 4: #as above
            ship_tail_2 = [x_value_2 +1, y_value_2]
            break
        if ship_direction_2 == 0 and y_value_2 < 4: #as above
            ship_tail_2 = [x_value_2, y_value_2 +1]
            break
    if ship_head_2 != ship_head_1 and ship_tail_2 != ship_tail_1 and ship_head_2 != ship_tail_1 and ship_tail_2 != ship_head_1:
        break

#starting values
shots_remaining = 15
win = False

#2D array of battleship grid for player #print grid and borders to player
grid = [
        ["A1", "B1", "C1", "D1", "E1"],
        ["A2", "B2", "C2", "D2", "E2"],
        ["A3", "B3", "C3", "D3", "E3"],
        ["A4", "B4", "C4", "D4", "E4"],
        ["A5", "B5", "C5", "D5", "E5"]
    ]
border = "---+----+----+----+---"

ship_grid = [
        ["A1", "B1", "C1", "D1", "E1"],
        ["A2", "B2", "C2", "D2", "E2"],
        ["A3", "B3", "C3", "D3", "E3"],
        ["A4", "B4", "C4", "D4", "E4"],
        ["A5", "B5", "C5", "D5", "E5"]
    ]

#assigns an x to the hidden grid at a ship's location
ship_grid[y_value_1][x_value_1] = "x "
if ship_direction_1 == 0:
    ship_grid[y_value_1 +1][x_value_1] = "x "
else:
    ship_grid[y_value_1][x_value_1 +1] = "x "

ship_grid[y_value_2][x_value_2] = "x "
if ship_direction_2 == 0:
    ship_grid[y_value_2 +1][x_value_2] = "x "
else:
    ship_grid[y_value_2][x_value_2 +1] = "x "

def grid_printing():
    print()
    print(" | ".join(grid[0]))
    print(border)
    print(" | ".join(grid[1]))
    print(border)
    print(" | ".join(grid[2]))
    print(border)
    print(" | ".join(grid[3]))
    print(border)
    print(" | ".join(grid[4]))
    print()
    
    
    
    
    if grid == ship_grid:
        win = True

#player menu where the player interacts and the computer responds
def player_menu():
    global shots_remaining
    start_game = True
    while start_game == True:
        #print bottom messages to player (shots remaining and next shot)
        print(f"You have {shots_remaining} shots remaining.")
        print()
        while True:
            x_input_check = input("Enter the vertical coordinate (1-5) of your next shot: ")
            if x_input_check.isdigit(): #will check to make sure the player did a proper integer input
                x_input = int(x_input_check) #now sets the x_input to be the good value
                if x_input >= 1 and x_input <= 5: #make sure in good range
                    x_input = x_input -1
                    break
                else:
                    print("Please enter a valid coordinate.")
            else:
                print("Please enter a valid coordinate.")

        #dictionary to store y letters to y numbers
        y_input_key ={
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4
        }
        while True:
            y_input_check = input("Enter the horizontal coordinate (A-E) of your next shot: ").capitalize()
            if y_input_check != "A" and y_input_check != "B" and y_input_check != "C" and y_input_check != "D" and y_input_check != "E": #needs to be looped so it doesnt continue after fail
                print("Please enter a valid coordinate.")
            else:
                y_input = y_input_key[y_input_check]
                shots_remaining -= 1
                break
        shot_coordinate = [x_input, y_input]
        if shot_coordinate == ship_head_1:
            grid[x_input][y_input] ="x "
        elif shot_coordinate == ship_tail_1:
            grid[x_input][y_input] ="x "
        elif shot_coordinate == ship_head_2:
            grid[x_input][y_input] ="x "
        elif shot_coordinate == ship_tail_2:
            grid[x_input][y_input] ="x "
        else:
            grid[x_input][y_input] ="o "
            ship_grid[x_input][y_input] ="o "
        
            
    #come back to add code that prevents you from firing on the same spot

starting_message()    
grid_printing()
player_menu()