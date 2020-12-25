def part1(num1, num2):
    loop = 0
    subject = 7
    value = 1
    while value != num1:
        value *= subject
        value = value % 20201227
        loop += 1
    print loop
    subject = num2
    value = 1
    for i in range(loop):
        value *= subject
        value = value % 20201227
    return value


print part1(5764801, 17807724)
print part1(12578151, 5051300)
