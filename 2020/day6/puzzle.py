def part1(filename):
    with open(filename) as f:
        s = set()
        count = 0
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line:
                for l in line:
                    s.add(l)
            else:
                count += len(s)
                s = set()
        count += len(s)
        return count


def part2(filename):
    with open(filename) as f:
        s = set()
        count = 0
        lines = f.readlines()
        first_person_in_group = True
        for line in lines:
            line = line.strip()
            if line:
                lineset = set()
                for l in line:
                    lineset.add(l)
                s = s.intersection(lineset)
                if first_person_in_group:
                    s = lineset
                    first_person_in_group = False
            else:
                count += len(s)
                s = set()
                first_person_in_group = True
        count += len(s)
        return count


print part2('input_sample.txt')
