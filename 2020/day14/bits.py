from collections import defaultdict


def read(filename):
    with open(filename) as f:
        return f.readlines()


def part1(filename):
    lines = read(filename)
    mem = defaultdict(int)
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
            and_mask = int(mask.replace('X', '1'), 2)
            or_mask = int(mask.replace('X', '0'), 2)
        elif line.startswith('mem'):
            address = int(line.split(' = ')[0].split('[')[1].split(']')[0])
            value = int(line.split(' = ')[1])
            mem[address] = (value & and_mask) | or_mask
        else:
            raise Exception('Invalid line: ' + line)
    return sum(list(mem.values()))


def part2(filename):
    lines = read(filename)
    mem = defaultdict(int)
    for line in lines:
        if line.startswith('mask'):
            mask = line.split(' = ')[1]
        elif line.startswith('mem'):
            address = int(line.split(' = ')[0].split('[')[1].split(']')[0])
            value = int(line.split(' = ')[1])
            address_bin = bin(address)[2:].zfill(36)
            filled_mask = []
            for i, j in zip(mask, address_bin):
                if i == '0':
                    filled_mask.append(j)
                elif i == '1':
                    filled_mask.append('1')
                elif i == 'X':
                    filled_mask.append(i)
            count = mask.count('X')
            for i in range(2 ** count):
                x = bin(i)[2:].zfill(count)
                xj = 0
                new_mask = []
                for mj in range(len(filled_mask)):
                    if filled_mask[mj] == 'X':
                        new_mask.append(x[xj])
                        xj += 1
                    else:
                        new_mask.append(filled_mask[mj])
                address = int(''.join(new_mask), 2)
                mem[address] = value
        else:
            raise Exception('Invalid line: ' + line)
    return sum(list(mem.values()))


print part2('input.txt')
