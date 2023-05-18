# Toy program to create terminal grid

rows = 10

grid = [list(range(1, 11)) for _ in range(rows)]

for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()
