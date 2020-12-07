def read_input(filename):
    l = []
    with open(filename) as f:
        for line in f.readlines():
            l.append(line.strip())
    return l


def convert(str):
    if len(str) != 10:
        raise Exception("Length must be 10")
    id = 0
    for s in str:
        if s == 'F' or s == 'L':
            id *= 2
        elif s == 'B' or s == 'R':
            id = id * 2 + 1
        else:
            raise Exception("Invalid str: " + str)
    return id


print convert('BFFFBBFRRR')
print convert('FFFBBBFRRR')
print convert('BBFFBBFRLL')


def find_last(filename):
    l = read_input(filename)
    ids = [convert(s) for s in l]
    ids.sort()
    return ids[-1]


print(find_last('input5.txt'))


def find_missing(filename):
    l = read_input(filename)
    ids = [convert(s) for s in l]
    ids.sort()
    print ids
    for i in range(ids[0], ids[-1]):
        if i != ids[i - ids[0]]:
            return i


print(find_missing('input5.txt'))
