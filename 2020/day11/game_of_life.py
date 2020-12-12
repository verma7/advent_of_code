import copy


def read(filename):
    grid = []
    with open(filename) as f:
        for line in f.readlines():
            l = []
            for char in line.strip():
                l.append(char)
            grid.append(l)
    return grid


def count_occupied_neighbors(grid, i, j):
    count = 0
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                if x != i or y != j:
                    if grid[x][y] == '#':
                        count += 1
    return count


def print_grid(grid):
    for i in range(len(grid)):
        print ''.join(grid[i])
    print


def count_grid(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                count += 1
    return count


def part1(filename):
    grid = read(filename)

    while True:
        next_grid = copy.deepcopy(grid)
        for i in range(len(next_grid)):
            for j in range(len(next_grid[0])):
                if grid[i][j] == '.':
                    next_grid[i][j] = '.'
                elif grid[i][j] == 'L' and count_occupied_neighbors(grid, i, j) == 0:
                    next_grid[i][j] = '#'
                elif grid[i][j] == '#' and count_occupied_neighbors(grid, i, j) >= 4:
                    next_grid[i][j] = 'L'
        print_grid(next_grid)
        if next_grid == grid:
            break
        grid = next_grid
    print count_grid(grid)


def count_occupied_neighbors2(grid, i, j):
    count = 0
    for xd, yd in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
        x = i
        y = j
        for step_x in range(max(len(grid), len(grid[0]))):
            x += xd
            y += yd
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                break
            if grid[x][y] == 'L':
                break
            if grid[x][y] == '#':
                count += 1
                break
    return count


def part2(filename):
    grid = read(filename)

    while True:
        next_grid = copy.deepcopy(grid)
        for i in range(len(next_grid)):
            for j in range(len(next_grid[0])):
                if grid[i][j] == '.':
                    next_grid[i][j] = '.'
                elif grid[i][j] == 'L' and count_occupied_neighbors2(grid, i, j) == 0:
                    next_grid[i][j] = '#'
                elif grid[i][j] == '#' and count_occupied_neighbors2(grid, i, j) >= 5:
                    next_grid[i][j] = 'L'
        print_grid(next_grid)
        if next_grid == grid:
            break
        grid = next_grid
    print count_grid(grid)


print part2('input.txt')
