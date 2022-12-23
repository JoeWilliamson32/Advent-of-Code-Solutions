import itertools
import math

data = open('input.txt').read().strip()
data = [x for x in data.split('\n')]

# Part 1 
elves = set()
for j in range(len(data)):
    for i in range(len(data[0])):
        if data[j][i] == '#':
            elves.add((i,j))

consider = [(0,1), (-1,1), (1,1),
            (0,-1), (-1,-1), (1,-1),
            (-1,0), (-1,-1), (-1,1), 
            (1,0), (1,-1), (1,1)
            ]

for _ in range(10):
    old = []
    new = []

    for x,y in elves:
        if all((x+dx, y-dy) not in elves for dx,dy in consider):
            old.append((x,y))
            new.append((x,y))

        else:
            for d1,d2,d3 in zip(*[iter(consider)]*3):
                check = 0
                dx1,dy1 = d1
                dx2, dy2 = d2
                dx3, dy3 = d3

                if (x+dx1, y-dy1) not in elves and (x+dx2, y-dy2) not in elves and (x+dx3, y-dy3) not in elves:
                    check += 1
                    old.append((x,y))
                    new.append((x+dx1, y-dy1))
                    break
                    
            if check == 0:
                old.append((x,y))
                new.append((x,y))
            
    

    coords = [] 
    
    for i in range(len(new)):
        if new.count(new[i]) > 1 :
            coords.append(old[i])
        else:
            coords.append(new[i])

    elves = set(coords)  

    consider = consider[3:] + consider[:3]

minx = math.inf
maxx = 0
miny = math.inf 
maxy = 0

for x,y in elves:
    minx = min(x, minx)
    maxx = max(x, maxx)
    miny = min(y, miny)
    maxy = max(y, maxy)
    
ans = ((maxx-minx+1) * (maxy-miny+1)) - len(elves) 
part1 = ans 


# Part 2 
elves = set()
for j in range(len(data)):
    for i in range(len(data[0])):
        if data[j][i] == '#':
            elves.add((i,j))
            
consider = [(0,1), (-1,1), (1,1),
            (0,-1), (-1,-1), (1,-1),
            (-1,0), (-1,-1), (-1,1), 
            (1,0), (1,-1), (1,1)]

ans = 1
for _ in range(2000):
    
    old = []
    new = []

    for x,y in elves:
        if all((x+dx, y-dy) not in elves for dx,dy in consider):
            old.append((x,y))
            new.append((x,y))

        else:
            for d1,d2,d3 in zip(*[iter(consider)]*3):
                check = 0
                dx1,dy1 = d1
                dx2, dy2 = d2
                dx3, dy3 = d3

                if (x+dx1, y-dy1) not in elves and (x+dx2, y-dy2) not in elves and (x+dx3, y-dy3) not in elves:
                    check += 1
                    old.append((x,y))
                    new.append((x+dx1, y-dy1))
                    break
                    
            if check == 0:
                old.append((x,y))
                new.append((x,y))

    coords = [] 

    
    for i in range(len(new)):
        if new.count(new[i]) > 1 :
            coords.append(old[i])
        else:
            coords.append(new[i])
            
    if new == old:
        break 
        
    elves = set(coords)  

    consider = consider[3:] + consider[:3]
    
    ans+=1

part2 = ans


print(part1)
print(part2)