data = open('input.txt').read().strip()
data = [int(x) for x in data.split('\n')]

# Part 1 
pos = [(num, i) for i,num in enumerate(data)]
# Store index values for duplicate values

for i, num in enumerate(data):
    idx = pos.index((num, i))
    val, _ = pos.pop(idx)
    new_idx = (idx+val) % len(pos)
    pos.insert(new_idx, (num,i))
    
pos = [x for x,y in pos]

pos_0 = pos.index(0)
total = 0
for number in [1000, 2000, 3000]:
    idx = (pos_0 + number) % (len(pos))
    val = pos[idx]
    total += val
part1 = total


# Part 2 
data = [x*811589153 for x in data]
pos = [(num, i) for i,num in enumerate(data)]

for _ in range(10):
    for i, num in enumerate(data):
        idx = pos.index((num, i))
        val, _ = pos.pop(idx)
        new_idx = (idx+val) % len(pos)
        pos.insert(new_idx, (num,i))
        
pos = [x for x,y in pos]

pos_0 = pos.index(0)
total = 0
for number in [1000, 2000, 3000]:
    idx = (pos_0 + number) % (len(pos))
    val = pos[idx]
    total += val
part2 = total

print(part1)
print(part2)
