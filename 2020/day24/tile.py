import math
from collections import defaultdict

sqrt_3_2 = round(math.sqrt(3) / 2, 3)
half = 1.0 / 2


def convert(str):
    x = 0
    y = 0
    i = 0
    while i < len(str):
        if str[i] == 'e':
            x += 1
            i += 1
        elif str[i] == 'w':
            x -= 1
            i += 1
        elif str[i] == 's' and str[i + 1] == 'e':
            x += half
            y -= sqrt_3_2
            i += 2
        elif str[i] == 'n' and str[i + 1] == 'w':
            x -= half
            y += sqrt_3_2
            i += 2
        elif str[i] == 's' and str[i + 1] == 'w':
            x -= half
            y -= sqrt_3_2
            i += 2
        elif str[i] == 'n' and str[i + 1] == 'e':
            x += half
            y += sqrt_3_2
            i += 2
        else:
            raise ValueError("Couldn't parse: " + str[i:])
    return tuple([round(x, 3), round(y, 3)])


def part1(filename):
    hex_is_white = defaultdict(lambda: True)
    with open(filename) as f:
        for line in f.readlines():
            idx = convert(line.strip())
            hex_is_white[idx] = not hex_is_white[idx]
    print hex_is_white
    count = 0
    for i in hex_is_white:
        if not hex_is_white[i]:
            count += 1
    return count


# print part1('input.txt')


def count_black_neigh(x, y, hex):
    count = 0
    for dx, dy in [(1, 0), (-1, 0), (half, sqrt_3_2), \
                   (-half, sqrt_3_2), (half, -sqrt_3_2), \
                   (-half, -sqrt_3_2)]:
        count += 0 if hex[(round(x + dx, 3), round(y + dy, 3))] else 1
    return count


def part2(filename):
    hex_is_white = defaultdict(lambda: True)
    with open(filename) as f:
        for line in f.readlines():
            idx = convert(line.strip())
            hex_is_white[idx] = not hex_is_white[idx]
    print hex_is_white
    for day in range(100):
        new_hex = hex_is_white.copy()
        for hx, hy in hex_is_white.keys():
            for dx, dy in [(1, 0), (-1, 0), (half, sqrt_3_2), \
                           (-half, sqrt_3_2), (half, -sqrt_3_2), \
                           (-half, -sqrt_3_2)]:
                x = round(hx + dx, 3)
                y = round(hy + dy, 3)
                neigh = count_black_neigh(x, y, hex_is_white)
                if hex_is_white[(x, y)] and neigh == 2:
                    new_hex[(x, y)] = False
                elif not hex_is_white[(x, y)] and (neigh == 0 or neigh > 2):
                    new_hex[(x, y)] = True
        hex_is_white = new_hex
        count = 0
        for i in hex_is_white:
            if not hex_is_white[i]:
                count += 1
        print day, count


print part2('input.txt')
