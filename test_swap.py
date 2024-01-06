from tower_swap import generate_random_grid, print_grid, swap 

grid = generate_random_grid()
print_grid(grid)


grid = swap(grid,2,2,"d")
print_grid(grid)

grid = swap(grid,2,2,"u")
print_grid(grid)

grid = swap(grid,2,2,"l")
print_grid(grid)

grid = swap(grid,2,2,"r")
print_grid(grid)


grid = swap(grid,0,2,"u")
print_grid(grid)

grid = swap(grid,5,3,"d")
print_grid(grid)

grid = swap(grid,3,0,"l")
print_grid(grid)

grid = swap(grid,3,5,"r")
print_grid(grid)