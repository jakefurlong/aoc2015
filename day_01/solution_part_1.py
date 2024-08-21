# solution.py

### Day 1 - Solution - Part 1###

with open('puzzle_input_part_1.txt', 'r') as file:
    content = file.read()

floor = 0

for c in content:
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

print(floor)