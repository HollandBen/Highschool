#Written by Ben Holland
#Date: 6 Feb 2024
#Battleship project

#importations
import random
global shots_hit, shots_remaining, start_game

#starting message and prompt to play the game
start_game = False
while start_game == False:
    print("Welcome to Battleship! \nYou are an elite commander tasked with sinking the two enemy ships that are hiding somewhere in the ocean. Every turn, submit coordinates to send an artillery shot towards the enemy. However, the allied supply lines were cut, and you only have 15 artillery shots to sink the enemy. \nIf your shot hits an enemy battleship, an x will appear, but if you miss, an o will appear.")
    startup = input("Press 1 to start the game: ")
    if startup.isdigit(): #will check to make sure the player did a proper integer input
        commence = int(startup) #
        if commence == 1:
            start_game = True
            break

#determine the x and y coordinates of the ship starters
while True:
    x_value_1 = random.randint(0,4)
    y_value_1 = random.randint(0,4)
    ship_direction_1 = random.randint(0,1) #0 is south, 1 is east
    ship_head_1 = [x_value_1, y_value_1]
    if ship_direction_1 != 0 or y_value_1 != 4: #prevents from spawning in a bad spot at bottom of board
        ship_tail_1 = [x_value_1, y_value_1 + 1]
        break #above and below currently have errors, it can spawn on border still
    
while True:
    while True:
        x_value_2 = random.randint(0,4)
        y_value_2 = random.randint(0,4)
        ship_direction_2 = random.randint(0,1) #0 is south, 1 is east
        ship_head_2 = [x_value_2, y_value_2]
        if ship_direction_2 != 0 or y_value_2 != 4: #prevents from spawning in a bad spot at bottom of board
            ship_tail_2 = [x_value_2, y_value_2 + 1]
            break
    if ship_head_2 != ship_head_1:
            break

#starting values
shots_remaining = 15
if shots_remaining == 0:
    start_game = False
shots_hit = 0
if shots_hit == 4:
    start_game = False
shots_missed = 0

#2D array of battleship grid for player
grid = [
    [" A1", "A2", "A3", "A4", "A5"],
    [" B1", "B2", "B3", "B4", "B5"],
    [" C1", "C2", "C3", "C4", "C5"],
    [" D1", "D2", "D3", "D4", "D5"],
    [" E1", "E2", "E3", "E4", "E5"]
]
border = "----+----+----+----+----"

#print grid and borders to player
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






while start_game == True:
    #print bottom messages to player (shots remaining and next shot)
    print("You have " + str(shots_remaining) + " shots remaining.")
    print()
    while True:
        x_input_check = input("Enter the x coordinate (1-5) of your next shot: ")
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
        y_input_check = input("Enter the y coordinate (A-E) of your next shot: ").capitalize()
        if y_input_check != "A" and y_input_check != "B" and y_input_check != "C" and y_input_check != "D" and y_input_check != "E": #needs to be looped so it doesnt continue after fail
            print("Please enter a valid coordinate.")
        else:
            y_value = y_input_key[y_input_check]
            shots_remaining += -1 #this does not work right now
            break
        
#come back to add code that prevents you from firing on the same spot