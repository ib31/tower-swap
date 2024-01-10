from tower_swap import print_grid, check_match, generate_random_grid
# from tower_swap import match_5v, match_5h, match_4v, match_4h, match_3v, match_3h

# grid = [[i * 6 + j for j in range(6)] for i in range(6)]

grid = generate_random_grid()

# grid[0][0:5]=[1]*5
# grid[1][2] = 1
# grid[2][2] = 1

# grid[0][1:6]=[1]*5
# grid[1][3] = 1
# grid[2][3] = 1

# grid[5][0:5]=[1]*5
# grid[4][2] = 1
# grid[3][2] = 1

grid[5][1:6]=[1]*5
grid[4][3] = 1
grid[3][3] = 1

# grid[0][0] = 0
# grid[0 + 1][0] = 0
# grid[0 + 2][0] = 0
# grid[0 + 3][0] = 0
# grid[0 + 4][0] = 0
# grid[0 + 2][1] = 0
# grid[0 + 2][2] = 0

# grid[1][0] = 0
# grid[1 + 1][0] = 0
# grid[1 + 2][0] = 0
# grid[1 + 3][0] = 0
# grid[1 + 4][0] = 0
# grid[1 + 2][1] = 0
# grid[1 + 2][2] = 0

# grid[0][5] = 0
# grid[0 + 1][5] = 0
# grid[0 + 2][5] = 0
# grid[0 + 3][5] = 0
# grid[0 + 4][5] = 0
# grid[0 + 2][4] = 0
# grid[0 + 2][3] = 0

# grid[1][5] = 0
# grid[1 + 1][5] = 0
# grid[1 + 2][5] = 0
# grid[1 + 3][5] = 0
# grid[1 + 4][5] = 0
# grid[1 + 2][4] = 0
# grid[1 + 2][3] = 0

# grid[0][0:4]=[1]*4
# grid[1][2] = 1
# grid[2][2] = 1

# grid[0][1:5]=[1]*4
# grid[1][3] = 1
# grid[2][3] = 1

# grid[5][0:4]=[1]*4
# grid[4][2] = 1
# grid[3][2] = 1

# grid[5][1:5]=[1]*4
# grid[4][3] = 1
# grid[3][3] = 1

print_grid(grid)
print_grid(check_match(grid,(-1,-1))[0])