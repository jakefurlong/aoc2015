# soulution_part_1.py

### Solution - Day 2 - Part 1###


with open('puzzle_input_part_1.txt', 'r') as file:
    
    total = 0

    for line in file:
        str_dim = line.split('x')
        dimensions = [int(s) for s in str_dim]
        dimensions.sort()
    
        l = dimensions[0]
        w = dimensions[1]
        h = dimensions[2]

        scrap = l * w
        
        surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
        sub_total = surface_area + scrap
        total += sub_total

    print("Total =", total, "square feet of wrapping paper")
    