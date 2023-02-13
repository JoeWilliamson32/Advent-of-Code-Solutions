from collections import defaultdict

data = open('input.txt').read().strip().splitlines()

# Part 1
count = defaultdict(tuple)

for line in data:
    coord1, coord2 = line.split(' -> ')
    x1,y1 = coord1.split(',')
    x2,y2 = coord2.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            if (x1,y) in count:
                count[(x1,y)] += 1
            else:
                count[(x1,y)] = 1

    if y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            if (x,y1) in count:
                count[(x,y1)] += 1
            else:
                count[(x,y1)] = 1


sum = 0 
for key, value in count.items():
    if value >= 2:
        sum += 1

part1 = sum

# Part 2 
count = defaultdict(tuple)

for line in data:
    coord1, coord2 = line.split(' -> ')
    x1,y1 = coord1.split(',')
    x2,y2 = coord2.split(',')
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    if x1 == x2:
        for y in range(min(y1,y2), max(y1,y2)+1):
            if (x1,y) in count:
                count[(x1,y)] += 1
            else:
                count[(x1,y)] = 1

    if y1 == y2:
        for x in range(min(x1,x2), max(x1,x2)+1):
            if (x,y1) in count:
                count[(x,y1)] += 1
            else:
                count[(x,y1)] = 1

    if abs(x1-x2) == abs(y1-y2):
        dy = y2 - y1
        dx = x2 - x1
        for x in range(min(x1,x2), max(x1,x2)+1):
            y = y1 + (x-x1)*(dy/dx)
            if (x,y) in count:
                count[(x,y)] += 1
            else:
                count[(x,y)] = 1

sum = 0 
for key, value in count.items():
    if value >= 2:
        sum += 1

part2 = sum


print(part1)
print(part2)
