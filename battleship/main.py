#Written by Ben Holland
#Date: 6 Feb 2024
#Battleship project

#importations
import random

#determine the x and y coordinates of the ship starters
while True:
    x_value_1 = random.randint(0,4)
    y_value_1 = random.randint(0,4)
    ship_direction_1 = random.randint(0,1)
    ship_head_1 = [x_value_1, y_value_1]
    if ship_direction_1 != 0 and y_value_1 != 4: #prevents from spawning in a bad spot at bottom of board
        break
    
while True:
    while True:
        x_value_2 = random.randint(0,4)
        y_value_2 = random.randint(0,4)
        ship_direction_2 = random.randint(0,1)
        ship_head_2 = [x_value_2, y_value_2]
        if ship_direction_2 != 0 or y_value_2 != 4: #prevents from spawning in a bad spot at bottom of board
            break
    if ship_head_2 != ship_head_1:
            break

#starting values
shots_remaining = 15
shots_hit = 0
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







#print bottom messages to player (shots remaining and next shot)
print("You have " + str(shots_remaining) + " shots remaining.")
print()
while True:
    x_input_check = input("Enter the x coordinate (1-5) of your next shot: ")
    if x_input_check.isdigit(): #will check to make sure the player did a proper integer input
        x_input = int(x_input_check) #now sets the x_input to be the good value
        if x_input >= 1 and x_input <= 5: #make sure in good range
            x_input = x_input -1
            print()
            break
        else:
            print("Please enter a valid coordinate.")
    else:
        print("Please enter a valid coordinate.")
while True:
    y_input = input("Enter the y coordinate (A-E) of your next shot: ").capitalize()
    if y_input != "A" and y_input != "B" and y_input != "C" and y_input != "D" and y_input != "E": #needs to be looped so it doesnt continue after fail
        print("Please enter a valid coordinate.")
    else:
        
        break
#come back and turn y letters into y numbers