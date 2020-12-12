def read(filename):
    l = []
    with open(filename) as f:
        for line in f.readlines():
            l.append(int(line.strip()))
    return l


def part1(filename):
    l = read(filename)
    l.append(0)
    l.sort()
    one_diff = 0
    three_diff = 1
    for i in range(len(l) - 1):
        diff = l[i + 1] - l[i]
        print diff
        if diff == 1:
            one_diff += 1
        elif diff == 3:
            three_diff += 1
        elif diff == 2:
            continue
        else:
            raise Exception("Found diff: " + str(diff))
    return one_diff * three_diff


def part2(filename):
    l = read(filename)
    l.append(0)
    l.sort()
    l.append(l[-1] + 3)
    print l[-1]
    dp = [0] * (l[-1] + 1)
    dp[0] = 1
    dp[1] = 1 if 1 in l else 0
    dp[2] = dp[0] + dp[1] if 2 in l else 0

    for i in l:
        if i >= 3:
            print i
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print dp
    return dp[i]


print part2('input.txt')
