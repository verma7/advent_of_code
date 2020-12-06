def get_grid(filename):
    with open(filename) as f:
        grid = []
        lines = f.readlines()
        for line in lines:
            grid.append(line.strip('\n'))
    return grid


def num_trees(grid, right, down):
    x = 0
    y = 0
    count = 0
    while y < len(grid):
        if grid[y][x] == '#':
            count += 1
        x = (x + right) % len(grid[0])
        y += down
    return count


def part1(filename):
    print num_trees(get_grid(filename), 3, 1)


def part2(filename):
    grid = get_grid(filename)
    output = 1
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        output *= num_trees(grid, right, down)
    return output


print part1("input3_sample.txt")
print part1("input3.txt")
print part2("input3_sample.txt")
print part2("input3.txt")
