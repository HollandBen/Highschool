#Written by Ben Holland
#Date: 6 Feb 2024
#testing

import random

#decides if the first ship will be placed South or East
ship_direction_1 = random.randint(0,1)

#decides if the second ship will be placed South or East
ship_direction_2 = random.randint(0,1)

#determine the x and y coordinates of the ship starters
x_value_1 = random.randint(0,4)
y_value_1 = random.randint(0,4)

x_value_2 = random.randint(0,4)
y_value_2 = random.randint(0,4)

#2D array of battleship grid
grid = [
    [A1, A2, A3, A4, A5]
    [B1, B2, B3, B4, B5]
    [C1, C2, C3, C4, C5]
    [D1, D2, D3, D4, D5]
    [E1, E2, E3, E4, E5]
]