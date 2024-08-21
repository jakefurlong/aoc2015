# solution_part_2.py

### Day 1 - Solution - Part 2###

with open('puzzle_input_part_1.txt', 'r') as file:
    content = file.read()

floor = 0
position = 1

for c in content:
    if c == "(":
        floor += 1
    elif c == ")":
        floor -= 1

    if floor < 0:
        print("Position is", position)
        break
    else:
        position += 1

print("Floor is", floor)