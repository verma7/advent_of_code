def read(filename):
    with open(filename) as f:
        rules = {}
        is_your_ticket = False
        is_nearby_ticket = False
        your_ticket = []
        nearby_tickets = []
        for line in f.readlines():
            if 'or' in line:
                # class: 1-3 or 5-7
                a = line.split(":")
                val = a[1].split(" or ")
                rules[a[0]] = (int(val[0].split("-")[0]), int(val[0].split("-")[1]), int(val[1].split("-")[0]),
                               int(val[1].split("-")[1]))
            elif "your ticket:" in line:
                is_your_ticket = True
            elif is_your_ticket:
                your_ticket = [int(i) for i in line.split(",")]
                is_your_ticket = False
            elif "nearby tickets" in line:
                is_nearby_ticket = True
            elif is_nearby_ticket:
                nearby_tickets.append([int(i) for i in line.split(",")])
    return rules, your_ticket, nearby_tickets


def part1(filename):
    rules, your_ticket, nearby_tickets = read(filename)
    sum = 0
    for ticket in nearby_tickets:
        for val in ticket:
            is_valid = False
            for l1, h1, l2, h2 in rules.values():
                if l1 <= val <= h1 or l2 <= val <= h2:
                    is_valid = True
            if not is_valid:
                print val
                sum += val
    return sum


def part2(filename):
    rules, your_ticket, nearby_tickets = read(filename)
    print rules
    print your_ticket
    print nearby_tickets

    possible = dict()
    for rule in rules:
        possible[rule] = set([i for i in range(len(rules))])

    for ticket in nearby_tickets:
        for index, val in enumerate(ticket):
            is_valid = False
            for l1, h1, l2, h2 in rules.values():
                if l1 <= val <= h1 or l2 <= val <= h2:
                    is_valid = True
            if is_valid:
                for rule, (l1, h1, l2, h2) in rules.items():
                    if not (l1 <= val <= h1 or l2 <= val <= h2):
                        if index in possible[rule]:
                            possible[rule].remove(index)

    print possible
    final = dict()
    while len(final) != len(rules):
        for rule in rules:
            if len(possible[rule]) == 1:
                final[rule] = possible[rule].pop()
                for r in rules:
                    if final[rule] in possible[r]:
                        possible[r].remove(final[rule])
    print final

    prod = 1
    for rule, index in final.items():
        if rule.startswith('departure'):
            prod *= your_ticket[index]
    return prod


print part2('input.txt')
