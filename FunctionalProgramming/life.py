def create_grid(rows, cols):
    return [[0] * cols for _ in range(rows)]


def initialize_grid(grid):
    # Set some initial live cells
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1:4] = [1] * 3


def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))


def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    neighbors = [(x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0]
    return sum(1 for nx, ny in neighbors if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1)


def update_grid(grid):
    new_grid = create_grid(len(grid), len(grid[0]))
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            neighbors = count_neighbors(grid, x, y)
            if grid[x][y] == 1:
                new_grid[x][y] = 1 if neighbors in (2, 3) else 0
            else:
                new_grid[x][y] = 1 if neighbors == 3 else 0
    return new_grid


def main():
    rows, cols = 5, 5
    grid = create_grid(rows, cols)
    initialize_grid(grid)
    print("Initial grid:")
    print_grid(grid)

    for _ in range(5):
        grid = update_grid(grid)
        print("\nUpdated grid:")
        print_grid(grid)


if __name__ == "__main__":
    main()
