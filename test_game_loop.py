from tower_swap import game_loop, generate_random_grid

grid =[[5, 4, 5, 5, 2, 3],
    [5, 3, 3, 4, 3, 5],
    [1, 4, 3, 1, 4, 5],
    [3, 5, 5, 2, 1, 4],
    [2, 1, 2, 4, 1, 4],
    [1, 4, 1, 5, 5, 3]]

# grid = generate_random_grid()

game_loop(grid)