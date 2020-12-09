def read(filename):
    program = []
    with open(filename) as f:
        for line in f.readlines():
            instruction = line.strip().split(' ')
            if len(instruction) != 2:
                raise Exception("Invalid instruction: ", instruction)
            program.append((instruction[0], int(instruction[1])))
    return program


def return_pc(program):
    pc = 0
    visited = set()
    accum = 0
    while pc != len(program):
        if pc in visited:
            print "Accum = ", accum
            return False, accum
        visited.add(pc)
        inst, data = program[pc]
        if inst == 'nop':
            pc += 1
        elif inst == 'acc':
            accum += data
            pc += 1
        elif inst == 'jmp':
            pc += data
        else:
            raise Exception("Unknown instruction: ", inst)
    return True, accum


def change_program(filename):
    program = read(filename)
    last = len(program)
    for i in range(last):
        if program[i][0] == 'nop':
            program[i] = ('jmp', program[i][1])
            ended, acc = return_pc(program)
            if ended:
                return acc
            program[i] = ('nop', program[i][1])
        elif program[i][0] == 'jmp':
            program[i] = ('nop', program[i][1])
            ended, acc = return_pc(program)
            if ended:
                return acc
            program[i] = ('jmp', program[i][1])
    return -1


print change_program('input.txt')
