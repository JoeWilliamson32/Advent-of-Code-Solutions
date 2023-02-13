data = open('input.txt').read().strip()
data = [x for x in data.split('\n')]

# Part 1 
unknowns = {}
knowns = {}
for line in data:
    monkey = line.split(':')[0]
    operation = line.split(':')[1].strip()
    
    try:
        operation = int(operation)
        knowns[monkey] = operation
    except:
        ValueError
        unknowns[monkey] = operation

while unknowns:
    knowns_copy = knowns.copy()
    unknowns_copy = unknowns.copy()
    for key, value in unknowns_copy.items():
        elem1, op, elem2 = value.split(' ')

        if elem1 in knowns_copy and elem2 in knowns_copy:
            val1 = knowns[elem1]
            val2 = knowns[elem2]
            cmd = str(val1) + op + str(val2)
            add = eval(cmd)
            knowns[key] = add
            unknowns.pop(key)
            
part1 = knowns['root']


# Part 2
unknowns = {}
knowns = {}
for line in data:
    monkey = line.split(':')[0]
    operation = line.split(':')[1].strip()
    
    try:
        operation = int(operation)
        knowns[monkey] = operation
    except:
        ValueError
        unknowns[monkey] = operation  

key1, _, key2 = unknowns['root'].split(' ')

while unknowns:
    knowns_copy = knowns.copy()
    unknowns_copy = unknowns.copy()
    for key, value in unknowns_copy.items():
        elem1, op, elem2 = value.split(' ')

        if elem1 in knowns_copy and elem2 in knowns_copy:
            val1 = knowns[elem1]
            val2 = knowns[elem2]
            
            if elem1 == 'humn':
                cmd = '(' + 'x' + op + str(val2) + ')'
                knowns[key] = cmd
                unknowns.pop(key)
                break
                
            elif elem2 == 'humn':
                cmd = '(' + str(val1) + op + 'x' + ')'
                knowns[key] = cmd
                unknowns.pop(key)
                break 
                
            else:    
                cmd = '(' + str(val1) + op + str(val2) + ')'
                if 'x' in (val1, val2):
                    knowns[key] = cmd
                    unknowns.pop(key)
                else:
                    knowns[key] = cmd
                    unknowns.pop(key)
            
    
if 'x' in knowns[key1]:
    target = eval(knowns[key2])
    eqn = knowns[key1]
else:
    target = eval(knowns[key1])
    eqn = knowns[key2]


l, r = 0, 100000000000000000000000000000
while l < r:
    mid = (l+r)//2
    
    x = mid
    ans = eval(eqn)
    
    if ans == target:
        break
        
    elif ans > target:
        l = mid+1
        
    else:
        r = mid - 1
        
part2 = mid


print(part1)
print(part2)
