# Toy program to generate terminal grid

import random

rows = 10
cols = 10

def generate_grid(rows:int, cols:int):
    # Fill each grid cell randomly with either 0 or 1 using a nested list comprehension
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return grid

def print_grid(grid):
    for row in grid:
        for cell in row:
            print(f"{cell}", end=" ")
        print()

grid = generate_grid(rows, cols)

print_grid(grid)
