def get_sum(x, y):
    return(x + y)


def get_mul(x, y):
    return(x * y)


with open('input.txt', 'r') as reader:
    inp = list(map(int, reader.read().split(',')))

inp[1] = 12
inp[2] = 2

BEGIN = 0
STEP = 4

OPCODE = {
    1: get_sum,
    2: get_mul
}

while inp[BEGIN] != 99:
    op_value = OPCODE[inp[BEGIN]](inp[inp[BEGIN + 1]], inp[inp[BEGIN + 2]])

    inp[inp[BEGIN + 3]] = op_value

    BEGIN += STEP

print(inp[0])
