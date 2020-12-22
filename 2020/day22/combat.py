def read(filename):
    deck1 = []
    deck2 = []
    player1 = False
    with open(filename) as f:
        for line in f.readlines():
            if "Player 1:" in line:
                player1 = True
            elif "Player 2:" in line:
                player1 = False
            elif line != "\n":
                if player1:
                    deck1.append(int(line))
                else:
                    deck2.append(int(line))
    return deck1, deck2


def part1(filename):
    deck1, deck2 = read(filename)
    done = False
    final = []
    while not done:
        if deck1 and deck2:
            done = False
        else:
            break
        d1 = deck1.pop(0)
        d2 = deck2.pop(0)
        if d1 > d2:
            deck1.extend([d1, d2])
            final = deck1
        else:
            deck2.extend([d2, d1])
            final = deck2
        print d1, d2
    print deck1, deck2
    return compute(final)


def compute(deck):
    result = 0
    for i, d in enumerate(reversed(deck)):
        result += (i + 1) * d
    return result


def rcombat(deck1, deck2):
    seen = set()
    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in seen:
            return 1
        seen.add(tuple([tuple(deck1), tuple(deck2)]))

        d1 = deck1.pop(0)
        d2 = deck2.pop(0)
        if len(deck1) >= d1 and len(deck2) >= d2:
            winner = rcombat(deck1[:d1], deck2[:d2])
        else:
            winner = 1 if d1 > d2 else 2
        if winner == 1:
            deck1.extend([d1, d2])
        else:
            deck2.extend([d2, d1])
    return winner


def part2(filename):
    deck1, deck2 = read(filename)
    winner = rcombat(deck1, deck2)
    return compute(deck1) if winner == 1 else compute(deck2)


print part2('input.txt')
