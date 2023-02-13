import math

data = open('input.txt').read().strip()
data =  [x for x in data.split('\n')]

# Part 1 
grid = []
coords = set()
for r in range(len(data)):
    row = []
    for c in range(len(data[0])):
        row.append(int(data[r][c]))
        coords.add((r,c))
    grid.append(row)

def ifFlash(r,c, changed):
    count = 0
    for (dr,dc) in ((-1,0), (-1,1), (-1,-1), (0,1), (0,-1), (1,0), (1,1), (1,-1)):
        nr = r + dr
        nc = c + dc

        if (nr, nc) in coords:
            grid[nr][nc] += 1

            if grid[nr][nc] > 9:
                count += 1
                changed.add((nr, nc))
                grid[nr][nc] = -math.inf
                count += ifFlash(nr, nc, changed)

    return count 

flashes = 0
for _ in range(100):
    changed = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1 
            if grid[r][c] > 9 :
                flashes += 1
                changed.add((r,c))
                grid[r][c] = -math.inf
                flashes += ifFlash(r,c, changed)
                
    for r,c in changed:
        grid[r][c] = 0

part1 = flashes

# Part 2 
grid = []
coords = set()
for r in range(len(data)):
    row = []
    for c in range(len(data[0])):
        row.append(int(data[r][c]))
        coords.add((r,c))
    grid.append(row)
grid_size = len(grid) * len(grid[0])

flashes = 0
for i in range(1000):
    changed = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1 
            if grid[r][c] > 9 :
                flashes += 1
                changed.add((r,c))
                grid[r][c] = -math.inf
                flashes += ifFlash(r,c, changed)
    
    if len(changed) == grid_size:
        part2 = i+1
        break

    for r,c in changed:
        grid[r][c] = 0



print(part1)
print(part2)
    
