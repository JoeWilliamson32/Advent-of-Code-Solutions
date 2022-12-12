import collections 

data = open('input.txt').read().strip()
data = [x for x in data.split('\n')]

width = len(data[0])
height = len(data)
grid = [[0 for _ in range(width)] for _ in range(height)]
for y in range(height):
    for x in range(width):
        if data[y][x] == 'S':
            grid[y][x] = 1
        elif data[y][x] == 'E':
            grid[y][x] = 26
        else:
            grid[y][x] = ord(data[y][x]) - ord('a')+1

def aoc22_12_part1(data, i,j):
                
    queue = collections.deque([[(i,j)]])
    seen = set([(i,j)])
    width = len(data[0])
    height = len(data)
    path = []
    res = []
    while queue:
        path = queue.popleft()
        x,y = path[-1]
        if data[y][x] == 'E':
            res = path 
        for x2,y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0<=x2<width and 0<=y2<height and (x2,y2) not in seen:
                if grid[y2][x2] <= grid[y][x]+1:
                    queue.append(path+[(x2,y2)])
                    seen.add((x2,y2))
                    
    return res

def aoc22_12_part2(grid):

    minpath = 10000
    starting = [(i,j) for i in range(width) for j in range(height) if grid[j][i] == 1]
    for pos in starting:
        x,y = pos
        length = len(aoc22_12_part1(data, x, y))-1
        if length > 0:
            minpath = min(minpath, length)
            
    return minpath


part1 = len(aoc22_12_part1(data, 0,20))-1
part2 = aoc22_12_part2(grid)

print(part1)
print(part2)