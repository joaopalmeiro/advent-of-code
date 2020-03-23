from math import floor

with open('input.txt', 'r') as reader:
    inp = list(map(int, reader))

fuels = [floor(mass / 3) - 2 for mass in inp]
fuel = sum(fuels)

print(fuel)
