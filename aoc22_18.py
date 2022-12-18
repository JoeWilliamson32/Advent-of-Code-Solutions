from collections import deque
import math

data = open('input.txt').read().strip()
data = [x for x in data.split('\n')]

# Part 1
# Original method - didn't need to consider every vertex in hindsight - could just consider the half way point 
count = {}

for cube in data:
    x,y,z = eval(cube)
    bottom_face = frozenset(sorted(((x,y,z), (x+1,y,z), (x,y+1,z), (x+1,y+1,z))))
    top_face = frozenset(sorted(((x,y,z-1), (x+1,y,z-1), (x,y+1,z-1), (x+1,y+1,z-1))))
    front_face = frozenset(sorted(((x,y,z), (x,y+1,z), (x,y,z-1), (x,y+1,z-1))))
    back_face = frozenset(sorted(((x+1,y,z), (x+1,y+1,z), (x+1,y,z-1), (x+1,y+1,z-1))))
    left_face = frozenset(sorted(((x,y,z), (x+1,y,z), (x,y,z-1), (x+1,y,z-1))))
    right_face = frozenset(sorted(((x,y+1,z), (x+1,y+1,z), (x,y+1,z-1), (x+1,y+1,z-1))))
    
    faces = [bottom_face, top_face, front_face, back_face, left_face, right_face]
    
    for face in faces:
        if face not in count:
            count[face] = 1
        else:
            count[face] += 1
            
ans = 0
for _, value in count.items():
    if value == 1:
        ans += 1

part1 = ans


# Part 2 
count = {}

# Consider the half way point since many faces may share verticies
transformations = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]

minx = miny = minz = math.inf
maxx = maxy = maxz = -math.inf

lava = set()

for cube in data:
    x,y,z = eval(cube)
    
    lava.add(tuple((x,y,z)))
    
    minx = min(minx,x)
    maxx = max(maxx,x)
    miny = min(miny,y)
    maxy = max(maxy,y)
    minz = min(minz,z)
    maxz = max(maxz,z)
    
    for dx,dy,dz in transformations:
        face = (x+dx, y+dy, z+dz)
        
        if face not in count:
            count[face] = 1
        else:
            count[face] += 1
            
minx -= 1 
maxx += 1 
miny -= 1
maxy += 1
minz -= 1
maxz += 1

air_spaces = {(minx, miny, minz)}
queue = deque([(minx, miny, minz)])
transformations2 = [(x*2,y*2,z*2) for (x,y,z) in transformations]

while queue:
    x,y,z = queue.popleft()
    
    for dx,dy,dz in transformations2:
        xt, yt, zt = face = (x+dx, y+dy, z+dz)
        
        if not (minx <= xt <= maxx and miny <= yt <= maxy and minz <= zt <= maxz):
            continue
            
        if face in lava or face in air_spaces:
            continue
            
        air_spaces.add(face)
        queue.append(face)
        
free_slots = set()
for x,y,z in air_spaces:
    for dx,dy,dz in transformations:
        free_slots.add((x+dx, y+dy, z+dz))
        
ans2 = 0
for face, value in count.items():
    if face in free_slots and value == 1:
        ans2 += 1
part2 = ans2


print(part1)
print(part2)