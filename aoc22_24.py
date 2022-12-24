from collections import deque, defaultdict
import math

data = open('input.txt').read().strip().splitlines()

blizzard = defaultdict(list) 
for r, line in enumerate(data[1:]):
    for c, item in enumerate(line[1:]):
        if item == '<':
            blizzard[0].append((r,c))
        if item == '>':
            blizzard[1].append((r,c))
        if item == '^':
            blizzard[2].append((r,c))
        if item == 'v':
            blizzard[3].append((r,c))


# Part 1 
rt, ct = (len(data[1:])-1, len(data[0][1:])-1)
queue = deque([(0, -1, 0)])
lcm = r*c // math.gcd(r,c)
target = (rt, ct-1)
visited = set()

while queue:
    t, rc, cc = queue.popleft()
    t += 1
    exit = False
    
    for dr, dc in ((-1,0), (1,0), (0,-1), (0,1), (0,0)):
        nr = rc + dr
        nc = cc + dc
        
        if (nr, nc) == target:
            part1 = t
            exit = True
            break
            
        if (nr < 0 or nr >= rt or nc < 0 or nc >= ct) and (nr, nc) != (-1,0):
            continue
            
        for (idx, br, bc) in ((0,0,-1), (1,0,1), (2,-1,0), (3,1,0)):
            bliz_cr = (nr - br*t)%rt
            bliz_cc = (nc - bc*t)%ct
            if (bliz_cr, bliz_cc) in blizzard[idx]:
                break
                
        else:
            key = (nr, nc, t%lcm)
            if key in visited:
                continue
            
            visited.add(key)
            queue.append((t,nr,nc))
    
    if exit == True:
        break

# Part 2
rt, ct = (len(data[1:])-1, len(data[0][1:])-1)
queue = deque([(0, -1, 0, 0)])
lcm = r*c // math.gcd(r,c)
target = ((rt, ct-1), (-1,0), (rt,ct-1))
visited = set()

while queue:
    t, rc, cc, step = queue.popleft()
    t += 1
    exit = False
    
    for dr, dc in ((-1,0), (1,0), (0,-1), (0,1), (0,0)):
        nr = rc + dr
        nc = cc + dc
        
        nstep = step
        
        if (nr, nc) == target[step]:
            if step == 2:
                part2 = t
                exit = True
                break
            nstep += 1
            
        if (nr < 0 or nr >= rt or nc < 0 or nc >= ct) and (nr, nc) not in target:
            continue
            
        check = False
        if (nr,nc) not in target:
            for (idx, br, bc) in ((0,0,-1), (1,0,1), (2,-1,0), (3,1,0)):
                bliz_cr = (nr - br*t)%rt
                bliz_cc = (nc - bc*t)%ct
                if (bliz_cr, bliz_cc) in blizzard[idx]:
                    check = True
                    break

        if not check:
            key = (nr, nc, t%lcm, nstep)
            if key in visited:
                continue

            visited.add(key)
            queue.append((t,nr,nc, nstep))
    
    if exit == True:
        break


print(part1)
print(part2)