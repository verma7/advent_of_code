def read(filename):
    l = []
    with open(filename) as f:
        for line in f.readlines():
            l.append(line.strip())
    return l


def precedence(op):
    if op == '+' or op == '*':
        return 1
    return 0


def precedence2(op):
    if op == '+':
        return 2
    elif op == '*':
        return 1
    return 0


def pop_expr(ops, vals):
    op = ops.pop()
    val1 = vals.pop()
    val2 = vals.pop()
    if op == '+':
        result = val1 + val2
    elif op == '*':
        result = val1 * val2
    vals.append(result)


def evaluate(str):
    ops = []
    vals = []
    for i in str:
        if '0' <= i <= '9':
            vals.append(int(i))
        elif i == '(':
            ops.append(i)
        elif i == ')':
            while ops and ops[-1] != '(':
                pop_expr(ops, vals)
            if ops:
                ops.pop()
        elif i == '+' or i == '*':
            while ops and precedence2(ops[-1]) >= precedence2(i):
                pop_expr(ops, vals)
            ops.append(i)
    while ops:
        pop_expr(ops, vals)
    return vals[-1]


def part1(filename):
    l = read(filename)
    result = 0
    for expr in l:
        result += evaluate(expr)
    return result


print part1('input.txt')
