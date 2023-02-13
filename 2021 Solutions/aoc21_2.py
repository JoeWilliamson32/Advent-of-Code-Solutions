data = open('input.txt').read().strip().splitlines()

# Part 1
horz = 0
depth = 0

for line in data:
    dir, num = line.split(' ')

    if dir == 'forward':
        horz += int(num)
    
    elif dir == 'down':
        depth += int(num)

    else:
        depth -= int(num)


part1 = horz * depth


# Part 2
horz = 0
depth = 0
aim = 0

for line in data:
    dir, num = line.split(' ')

    if dir == 'forward':
        horz += int(num)
        depth += int(num)*aim
    
    elif dir == 'down':
        aim  += int(num)

    else:
        aim -= int(num)

part2 = horz * depth


print(part1)
print(part2)

