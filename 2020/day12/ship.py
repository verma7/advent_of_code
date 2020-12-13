def read(filename):
    l = []
    with open(filename) as f:
        for line in f.readlines():
            l.append((line[0], int(line[1:])))
    return l


def part1(filename):
    instructions = read(filename)
    x = 0
    y = 0
    cur_dir = 'E'
    directions = 'ESWN'
    delta = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    for dir, distance in instructions:
        if dir == 'R':
            cur_dir = directions[(directions.index(cur_dir) + distance / 90) % 4]
        elif dir == 'L':
            cur_dir = directions[(directions.index(cur_dir) - distance / 90) % 4]
        elif dir == 'F':
            dir = cur_dir
        if dir in delta:
            dx, dy = delta[dir]
            x += dx * distance
            y += dy * distance
    return abs(x) + abs(y)


def part2(filename):
    instructions = read(filename)
    x = 0
    y = 0
    waypoint_x = 10
    waypoint_y = 1
    delta = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
    for dir, distance in instructions:
        if dir == 'R':
            for step in range(distance / 90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif dir == 'L':
            for step in range(distance / 90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif dir == 'F':
            x += waypoint_x * distance
            y += waypoint_y * distance
        if dir in delta:
            dx, dy = delta[dir]
            waypoint_x += dx * distance
            waypoint_y += dy * distance
    return abs(x) + abs(y)


print part2('input.txt')
