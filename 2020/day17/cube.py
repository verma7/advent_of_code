from collections import defaultdict


def read(filename):
    l = []
    with open(filename) as f:
        for line in f.readlines():
            l.append(line.strip())
    return l


def neighbors(cube, x, y, z, w):
    count = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                for l in range(w - 1, w + 2):
                    if i == x and j == y and k == z and l == w:
                        continue
                    if cube[(i, j, k, l)] == '#':
                        count += 1
    return count


def part1(filename, cycle):
    l = read(filename)

    cube = defaultdict(lambda: '.')
    z = 0
    Xd = len(l)
    Yd = len(l[0])
    Z = 1

    for x in range(len(l)):
        for y in range(len(l[0])):
            cube[(x, y, z)] = l[x][y]
    print cube

    for i in range(1, cycle + 1):
        new_cube = defaultdict(lambda: '.')
        for z in range(-i, i + 1):
            for x in range(-i, Xd + i):
                for y in range(-i, Yd + i):
                    n = neighbors(cube, x, y, z)
                    if cube[(x, y, z)] == '#':
                        new_cube[(x, y, z)] = '#' if n == 2 or n == 3 else '.'
                    else:
                        new_cube[(x, y, z)] = '#' if n == 3 else '.'
        cube = new_cube

    count = 0
    for x, y, z in cube.keys():
        count += 1 if cube[(x, y, z)] == '#' else 0
    return count


def part2(filename, cycle):
    l = read(filename)

    cube = defaultdict(lambda: '.')
    z = 0
    w = 0
    Xd = len(l)
    Yd = len(l[0])

    for x in range(len(l)):
        for y in range(len(l[0])):
            cube[(x, y, z, w)] = l[x][y]
    print cube

    for i in range(1, cycle + 1):
        new_cube = defaultdict(lambda: '.')
        for w in range(-i, i + 1):
            for z in range(-i, i + 1):
                for x in range(-i, Xd + i):
                    for y in range(-i, Yd + i):
                        n = neighbors(cube, x, y, z, w)
                        if cube[(x, y, z, w)] == '#':
                            new_cube[(x, y, z, w)] = '#' if n == 2 or n == 3 else '.'
                        else:
                            new_cube[(x, y, z, w)] = '#' if n == 3 else '.'
        cube = new_cube

    count = 0
    for x, y, z, w in cube.keys():
        count += 1 if cube[(x, y, z, w)] == '#' else 0
    return count


print part2('input.txt', 6)
