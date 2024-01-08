import random
import copy

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


def match_5h(grid, i, j):
    reward = 0
    if grid[i][j] == 0:
        return grid, reward
    if j < 2 and grid[i][j : j + 5] == [grid[i][j]] * 5:
        reward = 5
        grid, modified = match_2v(grid, i, j)
        if modified:
            reward += 2
        grid[i][j : j + 5] = [0] * 5
    return grid, reward


def match_5v(grid, i, j):
    reward = 0
    if grid[i][j] == 0:
        return grid, reward
    if i < 2 and [grid[i + _][j] for _ in range(5)] == [grid[i][j]] * 5:
        reward = 5
        grid, modified = match_2h(grid, i, j)
        if modified:
            reward += 2
        grid[i][j] = 0
        grid[i + 1][j] = 0
        grid[i + 2][j] = 0
        grid[i + 3][j] = 0
        grid[i + 4][j] = 0

    return grid, reward


def match_4h(grid, i, j):
    reward = 0
    if grid[i][j] == 0:
        return grid, reward
    if j < 3 and grid[i][j : j + 4] == [grid[i][j]] * 4:
        reward = 4
        grid, modified = match_1v(grid, i, j)
        if not modified:
            grid, modified = match_2v(grid, i, j)
        if modified:
            reward += 2
        grid[i][j : j + 4] = [0] * 4

    return grid, reward


def match_4v(grid, i, j):
    reward = 0
    if grid[i][j] == 0:
        return grid, reward
    if i < 3 and [grid[i + _][j] for _ in range(4)] == [grid[i][j]] * 4:
        reward = 4
        grid, modified = match_1h(grid, i, j)
        if not modified:
            grid, modified = match_2h(grid, i, j)
        if modified:
            reward += 2
        grid[i][j] = 0
        grid[i + 1][j] = 0
        grid[i + 2][j] = 0
        grid[i + 3][j] = 0

    return grid, reward


def match_3h(grid, i, j):
    reward = 0
    if grid[i][j] == 0:
        return grid, reward
    if j < 4 and grid[i][j : j + 3] == [grid[i][j]] * 3:
        reward = 3
        grid, modified = match_special_case(grid, i, j)
        if not modified:
            grid, modified = match_1v(grid, i, j)
        if not modified:
            grid, modified = match_2v(grid, i, j)
        if modified:
            reward += 2
        grid[i][j : j + 3] = [0] * 3

    return grid, reward


def match_3v(grid, i, j):
    reward = 0
    if grid[i][j] == 0:
        return grid, reward
    if i < 4 and [grid[i + _][j] for _ in range(3)] == [grid[i][j]] * 3:
        reward = 3
        grid, modified = match_1h(grid, i, j)
        if not modified:
            grid, modified = match_2h(grid, i, j)
        if modified:
            reward += 2
        grid[i][j] = 0
        grid[i + 1][j] = 0
        grid[i + 2][j] = 0
    return grid, reward


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
    return grid, modified


def match_2v(grid, i, j):
    modified = False
    if i > 1:
        if grid[i - 1][j + 2] == grid[i - 2][j + 2] == grid[i][j]:
            grid[i - 1][j + 2] = 0
            grid[i - 2][j + 2] = 0
            modified = True
    elif i < 4:
        if grid[i + 1][j + 2] == grid[i + 2][j + 2] == grid[i][j]:
            grid[i + 1][j + 2] = 0
            grid[i + 2][j + 2] = 0
            modified = True
    return grid, modified


def match_2h(grid, i, j):
    modified = False
    if j > 1:
        if grid[i + 2][j - 1] == grid[i + 2][j - 2] == grid[i][j]:
            grid[i + 2][j - 1] = 0
            grid[i + 2][j - 2] = 0
            modified = True
    elif j < 4:
        if grid[i + 2][j + 1] == grid[i + 2][j + 2] == grid[i][j]:
            grid[i + 2][j + 1] = 0
            grid[i + 2][j + 2] = 0
            modified = True
    return grid, modified


def check_match(grid):
    total = 0
    for i in range(6):
        for j in range(6):
            grid, reward = match_5h(grid, i, j)
            grid, reward = match_5v(grid, i, j)
            total += reward
    for i in range(6):
        for j in range(6):
            grid, reward = match_4h(grid, i, j)
            grid, reward = match_4v(grid, i, j)
            total += reward
    for i in range(6):
        for j in range(6):
            grid, reward = match_3h(grid, i, j)
            grid, reward = match_3v(grid, i, j)
            total += reward

    return grid, total


def get_column(grid, column_index):
    column = [0] * len(grid)
    for i in range(len(grid)):
        column[i] = grid[i][column_index]
    return column


def column_update(grid, column_index, new_column):
    for i in range(len(grid)):
        grid[i][column_index] = new_column[i]

    return grid


def gravity(grid):
    for j in range(len(grid)):
        column = get_column(grid, j)

        obj = [x for x in column if x != 0]

        for i in range(len(grid)):
            if i < (len(grid) - len(obj)):
                column[i] = random.randint(1, 5)
            else:
                column[i] = obj[i - (len(grid) - len(obj))]

        grid = column_update(grid, j, column)

    return grid


def is_full(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                return False
    return True


def fix_point(grid):
    action_score = 0
    while True:
        grid = gravity(grid)
        grid, total = check_match(grid)
        action_score += total
        if is_full(grid):
            break

    return grid, action_score


def game_loop(grid):
    total_score = 0
    stop = int(input("number of actions:\n"))
    grid, initial_score = fix_point(grid)
    total_score += initial_score
    for l in range(stop):
        print_grid(grid)
        i, j = [int(k) for k in input("type position i j of the object:\n").split()]
        d = input("choose a direction where to move it :\n")
        grid = swap(grid, i, j, d)
        grid, action_score = fix_point(grid)
        total_score += action_score
    print(f"game over ! Total score = {total_score}")


def brute_force_action(grid):
    temp_grid = copy.deepcopy(grid)
    temp_grid, initial_score = fix_point(temp_grid)

    dir = ("u", "d", "l", "r")
    best_score = 0
    best_action = (0, 0, dir[0])

    for i in range(len(grid)):
        for j in range(len(grid)):
            for d in dir:
                test_grid = copy.deepcopy(temp_grid)

                test_grid = swap(test_grid, i, j, d)
                test_grid, action_score = fix_point(test_grid)

                if action_score > best_score:
                    best_score = action_score
                    best_action = (i, j, d)

    return best_action, best_score + initial_score

def symmetric_action(action):
    i,j,d = action
    if d == 'r':
        return i,j+1,'l'
    elif d == 'l':
        return i,j-1,'r'
    elif d == 'u':
        return i-1,j,'d'
    elif d == 'd':
        return i+1,j,'u'

def distribution_brute_force_test(grid, epsilon):
    distribution = dict()
    for _ in range(epsilon):
        result= brute_force_action(grid)
        result2 = symmetric_action(result[0]),result[1]
        if result in distribution.keys():
            distribution[result] += 1
        elif result2 in distribution.keys():
            distribution[result2] += 1
        else:
            distribution[result] = 1
    return distribution
