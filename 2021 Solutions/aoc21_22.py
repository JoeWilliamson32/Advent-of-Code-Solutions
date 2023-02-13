from tqdm import tqdm

data = open('input.txt').read().strip()
data = [x for x in data.split('\n')]

# Part 1 - too slow for Part 2 
instructions = []
for line in data:
    cmd, coords = line.split(' ')
    x,y,z = coords.strip().split(',')
    x = x.split('x=')[1]
    y = y.split('y=')[1]
    z = z.split('z=')[1]
    xmin, xmax = x.split('..')
    ymin, ymax = y.split('..')
    zmin, zmax = z.split('..')
    instruction = [cmd, (xmin, xmax), (ymin, ymax), (zmin, zmax)]
    instructions.append(instruction)

on = set()

for line in instructions:
    cur = set()
    cmd, x, y, z = line
    xmin, xmax = x
    ymin, ymax = y
    zmin, zmax = z

    xmin = max(-50, int(xmin))
    xmax = min(50, int(xmax))
    ymin = max(-50, int(ymin))
    ymax = min(50, int(ymax))
    zmin = max(-50, int(zmin))
    zmax = min(50, int(zmax))
    

    for x in range(xmin, xmax+1):
        for y in range(ymin, ymax+1):
            for z in range(zmin, zmax+1):
                cur.add((x,y,z))

    if cmd == 'on':
        on = on.union(cur) 

    else:
        on = on.difference(cur)

part1 = len(on)

# Part 2 
instructions = []
x_int = []
y_int = []
z_int =[]
for line in data:
    cmd, coords = line.split(' ')
    x,y,z = coords.strip().split(',')
    x = x.split('x=')[1]
    y = y.split('y=')[1]
    z = z.split('z=')[1]
    xmin, xmax = map(int, x.split('..'))
    ymin, ymax = map(int, y.split('..'))
    zmin, zmax = map(int, z.split('..'))
    instructions.append((cmd=='on', (xmin, xmax), (ymin, ymax), (zmin, zmax)))
    x_int.extend([xmin, xmax+1])
    y_int.extend([ymin, ymax+1])
    z_int.extend([zmin, zmax+1])

instructions.reverse()
x_int.sort()
y_int.sort()
z_int.sort()

count = 0
for x1, x2 in tqdm(zip(x_int, x_int[1:])):
    ins_x = [(a, x, y, z) for a, x, y, z in instructions if x[0] <= x1 <= x[1]]
    for y1, y2 in zip(y_int, y_int[1:]):
        ins_y = [(a, x, y, z) for a, x, y, z in ins_x if y[0] <= y1 <= y[1]]
        for z1, z2 in zip(z_int, z_int[1:]):
            if next((a for a, x, y, z in ins_y if z[0] <= z1 <= z[1]), False):
                count += (x2 - x1) * (y2 - y1) * (z2 - z1)

part2 = count


print(part1)
print(part2)