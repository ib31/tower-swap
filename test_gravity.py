from tower_swap import generate_random_grid, print_grid, gravity

grid =[[5, 4, 5, 5, 0, 3],
    [5, 3, 3, 4, 3, 5],
    [1, 4, 3, 1, 4, 5],
    [3, 5, 5, 2, 1, 0],
    [2, 0, 0, 0, 1, 0],
    [0, 4, 1, 5, 5, 0]]

print_grid(grid)

grid = gravity(grid)

print_grid(grid)