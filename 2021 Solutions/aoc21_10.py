data = open('input.txt').read().strip()
data = [x for x in data.split()]

pairs = {"{":"}", "(":")", "[":"]", "<":">"}
scores = {')':3, ']':57, '}':1197, '>':25137}

# Part 1 
illegal = []
for line in data:
    stack = []
    for elem in line:
        if elem in '{([<':
            stack.append(elem)
        elif len(stack)>0 and elem == pairs[stack[-1]]:
            stack.pop()
        else:
            illegal.append(elem)
            break

score = 0
for elem in illegal:
    score += scores[elem]

part1 = score

# Part 2
incomplete = []
for line in data:
    stack = []
    for elem in line:
        if elem in '{([<':
            stack.append(elem)
        elif len(stack)>0 and elem == pairs[stack[-1]]:
            stack.pop()
        else:
            stack = []
            break
    
    if len(stack)>0:
        incomplete.append(stack)

new_scores = {")":1, "]":2, "}":3, ">":4}
total_scores = []
for line in incomplete:
    score = 0
    for elem in line[::-1]:
        score = (score*5) + new_scores[pairs[elem]]
    total_scores.append(score)

part2 = sorted(total_scores)[(len(total_scores)-1)//2]


print(part1)
print(part2)
