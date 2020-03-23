from math import floor

with open('input.txt', 'r') as reader:
    inp = list(map(int, reader))

total_fuel = 0

while sum(inp) > 0:
    inp = [floor(mass / 3) - 2 if floor(mass / 3) -
           2 > 0 else 0 for mass in inp]
    total_fuel += sum(inp)

print(total_fuel)
