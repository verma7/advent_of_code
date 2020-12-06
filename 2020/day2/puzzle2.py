import re
from collections import defaultdict


def valid_passwords(filename):
    with open(filename) as f:
        lines = f.readlines()
        count = 0
        for line in lines:
            # 1-3 a: abcde
            m = re.match('(?P<min_count>\d+)\-(?P<max_count>\d+) (?P<char>[a-z]): (?P<password>[a-z]+)', line)
            if is_password_valid_part2(m.group('password'), m.group('char'), int(m.group('min_count')),
                                       int(m.group('max_count'))):
                count += 1
        return count


def is_password_valid(password, char, min_count, max_count):
    count = defaultdict(int)
    for p in password:
        count[p] += 1
    return min_count <= count[char] <= max_count


def is_password_valid_part2(password, char, index1, index2):
    return (password[index1 - 1] == char) ^ (password[index2 - 1] == char)


# Part 1:
print valid_passwords("input2.txt")
