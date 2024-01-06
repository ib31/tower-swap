import random

"""" the game board is a 6x6 grid. 
There are 5 basic objects represented using symbols (integers from 1 to 5).
The symbol 0 represent the absence of object and it means that at next step gravity will apply to the objects above.
When at least 3 objects are aligned the upper or leftest one is changed from X to XX where X is the symbol of the object :
- the grid is checked for each row*column
- when an object is checked, we look for two matching object to the right or downwards
- we also check crossing 3-matching identical objects 
The other ones are changed to 0.

At each step an object can be moved to a certain direction with specific conditions :
 - if the object is in left, right and bottom edge of the grid (the shore) then it can be moved outside the board. 
    Then the object disappears and its symbol is changed to 0
 - if it is in the top edge, the object cannot be moved upwards
 - otherwise the object can swap its place with another adjacent object since it is different

 After an object was moved, the grid is checked and since there is a 0 in the grid, the gravity applies to every object above.
 That means while there is at least a 0 in the grid :
 1. the 0 swaps position with the symbol above recursively while the symbol above is different than 0
 2. then every 0 is changed to a random symbol X
 3. then the grid is checked for 3 matching objects

"""


def print_grid(grid):
    for row in grid:
        print(row)
    print()


def generate_random_grid():
    return [[random.randint(1, 5) for _ in range(6)] for _ in range(6)]


def swap(grid, i, j, direction):
    if direction == "l":
        if j == 0:
            grid[i][j] = 0
        else:
            temp = grid[i][j]
            grid[i][j] = grid[i][j - 1]
            grid[i][j - 1] = temp
    elif direction == "r":
        if j == 5:
            grid[i][j] = 0
        else:
            temp = grid[i][j]
            grid[i][j] = grid[i][j + 1]
            grid[i][j + 1] = temp
    elif direction == "u":
        if i == 0:
            pass
        else:
            temp = grid[i][j]
            grid[i][j] = grid[i - 1][j]
            grid[i - 1][j] = temp
    elif direction == "d":
        if i == 5:
            grid[i][j] = 0
        else:
            temp = grid[i][j]
            grid[i][j] = grid[i + 1][j]
            grid[i + 1][j] = temp
    return grid


def check_horizontal(grid, i, j):
    if j < 2 and grid[i][j : j + 5] == [grid[i][j]] * 5:
        grid[i][j : j + 5] = [0] * 5
        if i < 4:
            m = [grid[i + 1][j + 2], grid[i + 2][j + 2]]
            if m == [grid[i][j]] * 2:
                grid[i + 1][j + 2] = 0
                grid[i + 2][j + 2] = 0
    elif j < 3 and grid[i][j : j + 4] == [grid[i][j]] * 4:
        grid[i][j : j + 4] = [0] * 4
        if i < 4:
            m1 = [grid[i + 1][j + 1], grid[i + 2][j + 1]]
            m2 = [grid[i + 1][j + 2], grid[i + 2][j + 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 1][j + 1] = 0
                grid[i + 2][j + 1] = 0
            elif m2 == [grid[i][j]] * 2:
                grid[i + 1][j + 2] = 0
                grid[i + 2][j + 2] = 0
            else:
                pass
    elif j < 4 and grid[i][j : j + 3] == [grid[i][j]] * 3:
        grid[i][j : j + 3] = [0] * 3
        if i < 4:
            m1 = [grid[i + 1][j], grid[i + 2][j]]
            m2 = [grid[i + 1][j + 2], grid[i + 2][j + 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 1][j] = 0
                grid[i + 2][j] = 0
            elif m2 == [grid[i][j]] * 2:
                grid[i + 1][j + 2] = 0
                grid[i + 2][j + 2] = 0
            else:
                pass


def check_vertical(grid, i, j):
    if i < 2 and [grid[i + _][j] for _ in range(5)] == [grid[i][j]] * 5:
        grid[i][j : j + 5] = [0] * 5
        if j > 1:
            m1 = [grid[i + 2][j - 1], grid[i + 2][j - 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 2][j - 1] = 0
                grid[i + 2][j - 2] = 0
        elif j < 4:
            m1 = [grid[i + 2][j + 1], grid[i + 2][j + 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 2][j + 1] = 0
                grid[i + 2][j + 2] = 0
    elif i < 3 and [grid[i + _][j] for _ in range(4)] == [grid[i][j]] * 4:
        grid[i][j : j + 4] = [0] * 4

        if j > 1:
            m1 = [grid[i + 1][j - 1], grid[i + 1][j - 2]]
            m2 = [grid[i + 2][j - 1], grid[i + 2][j - 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 1][j - 1] = 0
                grid[i + 1][j - 2] = 0
            elif m2 == [grid[i][j]] * 2:
                grid[i + 2][j - 1] = 0
                grid[i + 2][j - 2] = 0
        elif j < 4:
            m1 = [grid[i + 1][j + 1], grid[i + 1][j + 2]]
            m2 = [grid[i + 2][j - 1], grid[i + 2][j - 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 1][j + 1] = 0
                grid[i + 1][j + 2] = 0
            elif m2 == [grid[i][j]] * 2:
                grid[i + 2][j + 1] = 0
                grid[i + 2][j + 2] = 0
    elif i < 4 and [grid[i + _][j] for _ in range(3)] == [grid[i][j]] * 3:
        grid[i][j : j + 3] = [0] * 3
        if j > 0 and j < 4:
            m1 = [grid[i + 2][j - 2], grid[i + 2][j - 1], grid[i + 2][j + 1]]
            if m1 == [grid[i][j]] * 3:
                grid[i + 2][j - 2] = 0
                grid[i + 2][j - 1] = 0
                grid[i + 2][j + 1] = 0
        elif j > 1 and j < 5:
            m1 = [grid[i + 2][j - 1], grid[i + 2][j + 1], grid[i + 2][j + 2]]
            if m1 == [grid[i][j]] * 3:
                grid[i + 2][j - 1] = 0
                grid[i + 2][j + 1] = 0
                grid[i + 2][j + 2] = 0
        elif j > 1:
            m1 = [grid[i + 1][j - 1], grid[i + 1][j - 2]]
            m2 = [grid[i + 2][j - 1], grid[i + 2][j - 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 1][j - 1] = 0
                grid[i + 1][j - 2] = 0
            elif m2 == [grid[i][j]] * 2:
                grid[i + 2][j - 1] = 0
                grid[i + 2][j - 2] = 0
        elif j < 4:
            m1 = [grid[i + 1][j + 1], grid[i + 1][j + 2]]
            m2 = [grid[i + 2][j - 1], grid[i + 2][j - 2]]
            if m1 == [grid[i][j]] * 2:
                grid[i + 1][j + 1] = 0
                grid[i + 1][j + 2] = 0
            elif m2 == [grid[i][j]] * 2:
                grid[i + 2][j + 1] = 0
                grid[i + 2][j + 2] = 0


def match_5h(grid, i, j):
    if grid[i][j]==0:
        return grid
    if j < 2 and grid[i][j : j + 5] == [grid[i][j]] * 5:
        grid = match_2v(grid, i, j)
        grid[i][j : j + 5] = [0] * 5
    return grid


def match_5v(grid, i, j):
    if grid[i][j]==0:
        return grid
    if i < 2 and [grid[i + _][j] for _ in range(5)] == [grid[i][j]] * 5:
        grid = match_2h(grid, i, j)
        grid[i][j] = 0
        grid[i + 1][j] = 0
        grid[i + 2][j] = 0
        grid[i + 3][j] = 0
        grid[i + 4][j] = 0
    return grid


def match_4h(grid, i, j):
    if grid[i][j]==0:
        return grid
    if j < 3 and grid[i][j : j + 4] == [grid[i][j]] * 4:
        grid, modified = match_1v(grid, i, j)
        if not modified:
            grid = match_2v(grid, i, j)
        grid[i][j : j + 4] = [0] * 4
    return grid


def match_4v(grid, i, j):
    if grid[i][j]==0:
        return grid
    if i < 3 and [grid[i + _][j] for _ in range(4)] == [grid[i][j]] * 4:
        grid, modified = match_1h(grid, i, j)
        if not modified:
            grid = match_2h(grid, i, j)
        grid[i][j] = 0
        grid[i + 1][j] = 0
        grid[i + 2][j] = 0
        grid[i + 3][j] = 0
    return grid


def match_3h(grid, i, j):
    if grid[i][j]==0:
        return grid
    if j < 4 and grid[i][j : j + 3] == [grid[i][j]] * 3:
        grid,modified = match_special_case(grid,i,j)
        if not modified:
            grid, modified = match_1v(grid, i, j)
        if not modified:
            grid = match_2v(grid, i, j)
        grid[i][j : j + 3] = [0] * 3
    return grid


def match_3v(grid, i, j):
    if grid[i][j]==0:
        return grid
    if i < 4 and [grid[i + _][j] for _ in range(3)] == [grid[i][j]] * 3:
        grid, modified = match_1h(grid, i, j)
        if not modified:
            grid = match_2h(grid, i, j)
        grid[i][j] = 0
        grid[i + 1][j] = 0
        grid[i + 2][j] = 0
    return grid


def match_1h(grid, i, j):
    modified = False
    if j > 1:
        if grid[i + 1][j - 1] == grid[i + 1][j - 2] == grid[i][j]:
            grid[i + 1][j - 1] = 0
            grid[i + 1][j - 2] = 0
            modified = True
    elif j < 4:
        if grid[i + 1][j + 1] == grid[i + 1][j + 2] == grid[i][j]:
            grid[i + 1][j + 1] = 0
            grid[i + 1][j + 2] = 0
            modified = True
    return grid, modified


def match_1v(grid, i, j):
    modified = False
    if i > 1:
        if grid[i - 1][j + 2] == grid[i - 2][j + 2] == grid[i][j]:
            grid[i - 1][j + 1] = 0
            grid[i - 2][j + 1] = 0
            modified = True
    elif i < 4:
        if grid[i + 1][j + 2] == grid[i + 2][j + 2] == grid[i][j]:
            grid[i + 1][j + 1] = 0
            grid[i + 2][j + 1] = 0
            modified = True
    return grid, modified


def match_special_case(grid, i, j):
    modified = False
    if i < 4 and grid[i][j] == grid[i + 1][j] == grid[i + 2][j]:
        grid[i + 1][j] = 0
        grid[i + 2][j] = 0
        modified = True
    return grid,modified


def match_2v(grid, i, j):
    if i > 1:
        if grid[i - 1][j + 2] == grid[i - 2][j + 2] == grid[i][j]:
            grid[i - 1][j + 2] = 0
            grid[i - 2][j + 2] = 0
    elif i < 4:
        if grid[i + 1][j + 2] == grid[i + 2][j + 2] == grid[i][j]:
            grid[i + 1][j + 2] = 0
            grid[i + 2][j + 2] = 0
    return grid


def match_2h(grid, i, j):
    if j > 1:
        if grid[i + 2][j - 1] == grid[i + 2][j - 2] == grid[i][j]:
            grid[i + 2][j - 1] = 0
            grid[i + 2][j - 2] = 0
    elif j < 4:
        if grid[i + 2][j + 1] == grid[i + 2][j + 2] == grid[i][j]:
            grid[i + 2][j + 1] = 0
            grid[i + 2][j + 2] = 0
    return grid


def check_match(grid):
    for i in range(6):
        for j in range(6):
                grid = match_5h(grid,i,j)
                grid = match_5v(grid,i,j)
    for i in range(6):
        for j in range(6):
                grid = match_4h(grid,i,j)
                grid = match_4v(grid,i,j)
    for i in range(6):
        for j in range(6):
                grid = match_3h(grid,i,j)
                grid = match_3v(grid,i,j)

    return grid
