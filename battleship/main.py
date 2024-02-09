#Written by Ben Holland
#Date: 6 Feb 2024
#Battleship project

#importations
import random

#decides if the first ship will be placed South (0) or East (1)
ship_direction_1 = random.randint(0,1)

#decides if the second ship will be placed South (0) or East (1)
ship_direction_2 = random.randint(0,1)

#determine the x and y coordinates of the ship starters
x_value_1 = random.randint(0,4)
y_value_1 = random.randint(0,4)

x_value_2 = random.randint(0,4)
y_value_2 = random.randint(0,4)

#starting values
shots_remaining = 15

#2D array of battleship grid
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
x_input = input("Enter the x coordinate (1-5) of your next shot: ")
if x_input >= 1 and x_input <= 5:
    
else:
    print("Please input valid coordinates.")

y_input = input("Enter the y coordinate (A-E) of your next shot: ")