data = open('input.txt').read().strip().splitlines()

east = set()
south = set()
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '>':
            east.add((r,c))
        if data[r][c] == 'v':
            south.add((r,c))

row_len = len(data)
col_len = len(data[0])

i = 0
while True:
    i += 1

    new_east = set()
    new_south = set()

    for (r,c) in east:
        nc = (c+1) % col_len

        if (r,nc) not in east and (r,nc) not in south:
            new_east.add((r,nc))
        else:
            new_east.add((r,c))

    for (r,c) in south:
        nr = (r+1) % row_len

        if (nr,c) not in new_east and (nr,c) not in south:
            new_south.add((nr,c))
        else:
            new_south.add((r,c))

    if east == new_east and south == new_south:
        part1 = i
        break

    east = new_east.copy()
    south = new_south.copy()


print(part1)