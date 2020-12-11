def read_ints(filename):
    l = []
    with open(filename) as f:
        for line in f.readlines():
            l.append(int(line.strip()))
    return l


def two_sum(int_list, target):
    s = set(int_list)
    for i in s:
        if target - i in s:
            return True
    return False


def first_invalid(filename, lookback):
    l = read_ints(filename)
    for i in range(len(l) - lookback):
        if not two_sum(l[i: i + lookback], l[i + lookback]):
            return l[i + lookback]
    return -1


def find_contiguous(filename, target):
    l = read_ints(filename)
    for i in range(len(l)):
        for j in range(i, len(l)):
            if sum(l[i:j]) == target:
                return min(l[i:j]) + max(l[i:j])
    return -1


print first_invalid('input.txt', 25)
print find_contiguous('input_sample.txt', 5, 127)
print find_contiguous('input.txt', 50047984)
