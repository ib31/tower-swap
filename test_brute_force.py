from tower_swap import print_grid, distribution_brute_force_test, generate_random_grid

grid =[[5, 1, 4, 1, 4, 2],
       [3, 2, 3, 1, 4, 3],
       [1, 44, 2, 2, 5, 1],
       [5, 5, 3, 5, 3, 5],
       [2, 2, 1, 22, 1, 4],
       [11, 5, 1, 3, 2, 1]]

# grid = generate_random_grid()

print_grid(grid)

dist = distribution_brute_force_test(grid,1000)



d = dict()

for k in range(10):
    max_key, max_value = max(dist.items(), key=lambda x: x[1])
    d[max_key] = max_value
    dist.pop(max_key)

print(d)