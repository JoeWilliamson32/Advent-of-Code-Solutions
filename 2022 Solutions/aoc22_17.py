from tqdm import tqdm

data = open('input.txt').read()
flows = [x for x in data if x != '\n']

# Part 1 
def shape_generator(shape:str, maxY):
    if shape == 'shape1':
        shape = set((2+i, maxY+4) for i in range(4))
    if shape == 'shape2':
        shape = set(((3, maxY+6), (3, maxY+5), (3, maxY+4), (2, maxY+5), (4, maxY+5)))
    if shape == 'shape3':
        shape =  set(((2, maxY+4), (3, maxY+4), (4, maxY+4), (4, maxY+5), (4, maxY+6)))
    if shape == 'shape4':
        shape = set((2, maxY+4+i) for i in range(4))
    if shape == 'shape5':
        shape = set(((2, maxY+4), (2, maxY+5), (3, maxY+4), (3,maxY+5)))
        
    return shape

taken = set((i, 0) for i in range(7))
maxY = 0
shapes = ['shape1', 'shape2', 'shape3', 'shape4', 'shape5']

for _ in range(2022):
    shape = shapes[0]
    shape_ = shape
    shape = shape_generator(shape, maxY)
    shapes.pop(0)
    
    while True:
        flow = flows[0]
        xMax = max(shape, key = lambda x:x[0])[0]
        xMin = min(shape, key = lambda x:x[0])[0]
        yMax = max(shape, key = lambda x:x[1])[1]
        yMin = min(shape, key = lambda x:x[1])[1]
        
        if flow == '>' and xMax + 1 < 7:
            shape_test = set((x+1, y) for x,y in shape)
            if not shape_test.intersection(taken):
                shape = shape_test
                xMax += 1
                
        elif flow == '<' and xMin -1 >= 0:
            shape_test = set((x-1, y) for x,y in shape)
            if not shape_test.intersection(taken):
                shape = shape_test
                xMin -= 1
                
        flows.pop(0)
        flows.append(flow)
                
        shape_test = set((x, y-1) for x,y in shape)
        if not shape_test.intersection(taken):
            shape = shape_test
        else:
            break
            
    
    yMax = max(shape, key = lambda x:x[1])[1]
    maxY = max(maxY, yMax)
    taken.update(shape)
    shapes.append(shape_)

part1 = maxY
print(part1)

# Part 2 - too many iterations, need to find a pattern and skip to end
def formation(taken):
    maxY = max([y for (x,y) in taken])
    return frozenset([(x,maxY-y) for (x,y) in taken if maxY-y<=30])

taken = set((i, 0) for i in range(7))
maxY = 0
shapes = ['shape1', 'shape2', 'shape3', 'shape4', 'shape5']
seen = {}
i = 0 
t = 0
added = 0


while i < 1000000000000:
    shape = shapes[0]
    shape_ = shape
    shape = shape_generator(shape, maxY)
    shapes.pop(0)
    
    while True:
        flow = flows[0]
        xMax = max(shape, key = lambda x:x[0])[0]
        xMin = min(shape, key = lambda x:x[0])[0]
        yMax = max(shape, key = lambda x:x[1])[1]
        yMin = min(shape, key = lambda x:x[1])[1]
        
        if flow == '>' and xMax + 1 < 7:
            shape_test = set((x+1, y) for x,y in shape)
            if not shape_test.intersection(taken):
                shape = shape_test
                xMax += 1
                
        elif flow == '<' and xMin -1 >= 0:
            shape_test = set((x-1, y) for x,y in shape)
            if not shape_test.intersection(taken):
                shape = shape_test
                xMin -= 1
                
        flows.pop(0)
        flows.append(flow)
                
        shape_test = set((x, y-1) for x,y in shape)
        if not shape_test.intersection(taken):
            shape = shape_test
        else:
            break
      
    
    yMin = min(shape, key = lambda x:x[1])[1]
    yMax = max(shape, key = lambda x:x[1])[1]
    maxY = max(maxY, yMax)
    taken.update(shape)
    shapes.append(shape_)
    
    t = i % len(flows)
    sig = (flows[t], i%5, formation(taken))
    if sig in seen:
        old_i, old_y = seen[sig]
        dy = maxY - old_y
        dt = i - old_i
        amt = (1000000000000-i)//dt
        added += amt*dy
        i+=amt*dt
    seen[sig] = (i, maxY)
    i += 1

part2 = maxY+added 

print(part1)
print(part2)
