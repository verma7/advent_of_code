def read(filename):
    n = 0
    bus = []
    with open(filename) as f:
        n = int(f.readline())
        bus = f.readline().split(',')
        bus = [int(b) if b != 'x' else None for b in bus]
    return n, bus


def part1(filename):
    n, buses = read(filename)
    print n, buses
    for i in range(n, 2 * n):
        for bus in buses:
            if bus and i % bus == 0:
                return bus * (i - n)
    return -1


def part2(filename):
    _, buses = read(filename)
    b = {}
    for i, bus in enumerate(buses):
        if bus:
            b[bus] = i

    min_value = 0
    running_product = 1
    for bus, remainder in b.items():
        while (min_value + remainder) % bus != 0:
            min_value += running_product
        running_product *= bus
        print min_value
    return min_value


print part2('input.txt')
