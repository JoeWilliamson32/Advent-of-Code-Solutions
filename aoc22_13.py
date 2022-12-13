from functools import cmp_to_key

data = open('input.txt').read().strip().split('\n\n')
data = list(map(str.splitlines, data))

def compare(l,r):
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return -1
        elif l == r:
            return 0
        else:
            return 1
        
    elif isinstance(l, list) and isinstance(r, int):
        return compare(l, [r])
    
    elif isinstance(l, int) and isinstance(r, list):
        return compare([l], r)
    
    else:
        i = 0
        while i<len(l) and i<len(r):
            item = compare(l[i], r[i])
            if item == -1:
                return -1
            if item == 1:
                return 1 
            i += 1
        if i==len(l) and i<len(r):
            return -1
        elif i==len(r) and i<len(l):
            return 1
        else:
            return 0
                    

part1 = 0
for i, (l, r) in enumerate(data):
    l = eval(l)
    r = eval(r)
    if compare(l,r) == -1:
        part1 += i + 1



data2 = list(map(eval, open('input.txt').read().split()))
data2.append([[2]])
data2.append([[6]])
data2 = sorted(data2, key=cmp_to_key(lambda l,r: compare(l,r)))

part2 = 1
for i, item in enumerate(data2):
    if item == [[2]] or item == [[6]]:
        part2 *= i+1

print(part1)
print(part2)