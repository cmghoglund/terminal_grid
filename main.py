# Toy program to generate terminal grid

import random

rows = 10
cols = 10

def generate_grid(rows:int, cols:int):
    # Fill each grid cell with a random number 1-10 using a nested list comprehension
    grid = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]
    return grid

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(f"{cell:2d}", end=" ") # Right-align numbers with each having a width of 2
        print()

grid = generate_grid(rows, cols)

print_grid(grid)
