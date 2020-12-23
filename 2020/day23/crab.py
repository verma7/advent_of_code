def part1(inp, moves):
    cups = [int(i) for i in inp]
    min_cup = min(cups)
    max_cup = max(cups)
    L = len(cups)
    for i in range(moves):
        print "-- move ", i + 1
        print cups
        current = cups[0]
        three_cups = cups[1:4]
        del cups[1:4]
        print three_cups
        destination = current - 1
        if destination < min_cup:
            destination = max_cup
        while destination in three_cups:
            destination -= 1
            if destination < min_cup:
                destination = max_cup
        print "Destination = ", destination
        dest_index = cups.index(destination)
        cups = cups[1:dest_index + 1] + three_cups + cups[dest_index + 1:] + [cups[0]]
        print cups
    ind = cups.index(1)
    res = cups[(ind + 1):] + cups[:ind]
    print res
    return ''.join(str(i) for i in res)


def part2(inp, moves, n):
    cups = [int(i) for i in inp]
    min_cup = min(cups)
    max_cup = max(cups)
    i = max_cup
    for i in range(max_cup + 1, n + 1):
        cups.append(i)
    max_cup = max(cups)
    ring = {}
    for i in range(len(cups)):
        if i == len(cups) - 1:
            ring[cups[i]] = cups[0]
        else:
            ring[cups[i]] = cups[i + 1]
    current = cups[0]
    for i in range(moves):
        three_cups = []
        next = ring[current]
        for k in range(3):
            three_cups.append(next)
            next = ring[next]
        ring[current] = next
        destination = current - 1
        if destination < min_cup:
            destination = max_cup
        while destination in three_cups:
            destination -= 1
            if destination < min_cup:
                destination = max_cup
        stitch = ring[destination]
        ring[destination] = three_cups[0]
        ring[three_cups[2]] = stitch

        current = ring[current]

    res = ring[1] * ring[ring[1]]
    return res


print part2('598162734', int(1e7), int(1e6))
