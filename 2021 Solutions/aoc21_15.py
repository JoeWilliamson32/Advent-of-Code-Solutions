from collections import defaultdict
from heapq import heappop, heappush
import math 

data = open('input.txt').read().strip().splitlines()
grid = []
grid_coords = set()
for r in range(len(data)):
    row = []
    for c in range(len(data[0])):
        row.append(int(data[r][c]))
        grid_coords.add((r,c))
    grid.append(row)

# Part 1 
unvisited = grid_coords.copy()
target = (r, c)
risk_value = defaultdict(lambda: math.inf)
risk_value[(0,0)] = 0
queue = []
heappush(queue, (0, (0,0)))

while target in unvisited:
    cur_risk, pos = heappop(queue)
    r,c = pos 

    if (r,c) not in unvisited:
        continue

    for dr,dc in ((-1,0), (1,0), (0,-1), (0,1)):
        nr = r + dr
        nc = c + dc

        if (nr, nc) not in grid_coords or (nr,nc) not in unvisited:
            continue

        nrisk = min(risk_value[(nr,nc)], cur_risk + grid[nr][nc])
        risk_value[(nr,nc)] = nrisk
        heappush(queue, (nrisk, (nr,nc)))

    unvisited.remove((r,c))

part1 = risk_value[target]

     
# Part 2
tile_width = len(grid[0])
tile_height = len(grid)
total_width = tile_width*5
total_height = tile_height*5

full_grid = []
grid_coords = set()
for r in range(total_height):
    row = []
    for c in range(total_width):
        r_sf = r // tile_height
        c_sf = c // tile_width

        val = grid[r%tile_height][c%tile_width]
        val = (val + r_sf + c_sf -1) % 9 + 1
        row.append(val)
        grid_coords.add((r,c))

    full_grid.append(row)

unvisited = grid_coords.copy()
target = (len(full_grid)-1, len(full_grid[0])-1)
risk_value = defaultdict(lambda: math.inf)
risk_value[(0,0)] = 0
queue = []
heappush(queue, (0, (0,0)))

while target in unvisited:
    cur_risk, pos = heappop(queue)
    r,c = pos 

    if (r,c) not in unvisited:
        continue

    for dr,dc in ((-1,0), (1,0), (0,-1), (0,1)):
        nr = r + dr
        nc = c + dc

        if (nr, nc) not in grid_coords or (nr,nc) not in unvisited:
            continue

        nrisk = min(risk_value[(nr,nc)], cur_risk + full_grid[nr][nc])
        risk_value[(nr,nc)] = nrisk
        heappush(queue, (nrisk, (nr,nc)))

    unvisited.remove((r,c))

part2 = risk_value[target]


print(part1)
print(part2)




