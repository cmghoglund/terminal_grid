# Toy program to create terminal grid

import random

rows = 10
cols = 10

# Fill each grid cell with a random number 1-10 using a nested list comprehension
grid = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

for row in grid:
    for cell in row:
        print(f"{cell:2d}", end=" ") # Right-align numbers with each having a width of 2
    print()
