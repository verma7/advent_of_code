from collections import defaultdict


def part1(num, n):
    ans = []
    idx = defaultdict(list)
    for i in range(len(num)):
        idx[num[i]].append(i + 1)
    last = num[-1]
    print "last = ", last
    i = len(num)
    while i <= n:
        i += 1

        if last not in idx:
            last = 0
        else:
            if len(idx[last]) == 1:
                last = 0
            else:
                last = idx[last][-1] - idx[last][-2]
        idx[last].append(i)
        ans.append(str(last))
    return ans


def part2(num, n):
    prev = defaultdict(int)
    prev_prev = defaultdict(int)
    for i in range(len(num)):
        prev[num[i]] = i + 1
    last = num[-1]
    print "last = ", last
    i = len(num)
    while i <= n:
        i += 1

        if last not in prev:
            last = 0
        else:
            if last not in prev_prev or prev_prev[last] == 0:
                last = 0
            else:
                last = prev[last] - prev_prev[last]
        prev_prev[last] = prev[last]
        prev[last] = i
        if i % 100000 == 0:
            print last
    return last


print part2([14, 3, 1, 0, 9, 5], 30000000 - 1)
