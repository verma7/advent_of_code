def read(filename):
    rule = True
    rules = {}
    input = []
    with open(filename) as f:
        for line in f.readlines():
            if rule:
                rules[line.split(':')[0]] = line.split(':')[1].strip()
            elif line == "\n":
                rule = False
            else:
                input.append(line.strip())
    return rules, input


def match(rules, str, rule):
    if rules[rule].contains('"'):
        if str[0] == rule[1] and len(str) == 1:
            return [str[1:]]
    else:
        result = []
        for x in rules[rule]:
            zm = [str]
            for r in x:

        elif rule.contains("|"):
        r = rule.split("|")
        left = match(rules, str, r[0])
        right = match(rules, str, r[1])
        return left or right
    else:
    rs = rule.split(" ")
    matches = True
    for r in rs:
        m, x = match(rules, str, r, i)
        if m:
            i = x
        else:
            return False


def parse(filename):
    rules, input = read(filename)
    count = 0
    for i in input:
        if match(rules, i, rules[0]):
            count += 1
    return count
