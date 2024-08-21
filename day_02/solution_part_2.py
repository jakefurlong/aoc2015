# solution_part_2.py

### Day 2 - Solution - Part 2 ###

with open('puzzle_input_part_1.txt', 'r') as file:
    
    total = 0

    for line in file:
        str_dim = line.split('x')
        dimensions = [int(s) for s in str_dim]
        dimensions.sort()
    
        l = dimensions[0]
        w = dimensions[1]
        h = dimensions[2]

        volume = l * w * h
        smallest_perimeter = (2 * l) + (2 * w)
        
        sub_total = volume + smallest_perimeter
        total += sub_total

    print(total)