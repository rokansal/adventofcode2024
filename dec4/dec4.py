grid = []
with open("dec4/input.txt") as file:
    for line in file:
        grid.append([])
        for char in line:
            if char.isalnum():
                grid[-1].append(char)

#part 1 find "xmas"
counter = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "X":
            ways = [(1,0), (1,1), (0,1), (0,-1), (-1,0), (-1,-1), (1, -1), (-1, 1)]
            for way in ways:
                R = r + 3 * way[0]
                C = c + 3 * way[1]
                if not (R < 0 or C < 0 or R >= len(grid) or C >= len(grid[0])):
                    if (grid[r + 1 * way[0]][c + 1 * way[1]] == "M"):
                        if (grid[r + 2 * way[0]][c + 2 * way[1]] == "A"):
                            if (grid[r + 3 * way[0]][c + 3 * way[1]] == "S"):
                                counter += 1
print(counter)

#part 2 find "x-mas" (two crossed "mas" strings)
counter = 0
for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0]) - 1):
        if grid[r][c] == "A":
            if ((grid[r-1][c-1] == "M" and grid[r+1][c+1] == "S") or (grid[r-1][c-1] == "S" and grid[r+1][c+1] == "M")):
                if ((grid[r+1][c-1] == "M" and grid[r-1][c+1] == "S") or (grid[r+1][c-1] == "S" and grid[r-1][c+1] == "M")):
                    counter += 1
print(counter)