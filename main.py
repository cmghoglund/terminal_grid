# Toy program to create terminal grid

rows = 10

grid = []

for _ in range(rows):
    row = list(range(1, 11))
    grid.append(row)

for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()
