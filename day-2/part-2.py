def get_sum(x, y):
    return(x + y)


def get_mul(x, y):
    return(x * y)


with open('input.txt', 'r') as reader:
    raw_inp = list(map(int, reader.read().split(',')))

STEP = 4
HALT = 99

OPCODE = {
    1: get_sum,
    2: get_mul
}

for noun in range(100):
    for verb in range(100):
        BEGIN = 0
        inp = raw_inp.copy()

        inp[1] = noun
        inp[2] = verb

        while inp[BEGIN] != HALT:
            op_value = OPCODE[inp[BEGIN]](
                inp[inp[BEGIN + 1]], inp[inp[BEGIN + 2]])

            inp[inp[BEGIN + 3]] = op_value

            BEGIN += STEP

        if inp[0] == 19690720:
            print(100 * noun + verb)
            break
