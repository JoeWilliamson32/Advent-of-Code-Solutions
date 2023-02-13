data = open('input.txt').read().strip().splitlines()


# Part 1
p1_pos = int(data[0].split(': ')[1])
p2_pos = int(data[1].split(': ')[1])
p1_score = 0
p2_score = 0

i = 1
count = 0

while True:
    p1_rolls = 0
    for j in range(i, i+3):
        p1_rolls += (j-1) % 10 + 1 
    
    p1_pos = (p1_pos + p1_rolls - 1) % 10 + 1
    p1_score += p1_pos

    i = (i + 3 - 1) % 100 + 1
    count += 3

    if p1_score >= 1000:
        break

    p2_rolls = 0
    for j in range(i, i+3):
        p2_rolls += (j-1) % 10 + 1 
    
    p2_pos = (p2_pos + p2_rolls - 1) % 10 + 1
    p2_score += p2_pos

    i = (i + 3 - 1) % 100 + 1
    count += 3

    if p2_score >= 1000:
        break

part1 = min(p1_score, p2_score) * count


# Part 2 
p1_pos = int(data[0].split(': ')[1])
p2_pos = int(data[1].split(': ')[1])
p1_score = 0
p2_score = 0
states = {}

def count_winners(p1_pos, p2_pos, p1_score, p2_score):
    if p1_score >= 21:
        return (1,0)
    if p2_score >= 21:
        return (0,1)

    if (p1_pos, p2_pos, p1_score, p2_score) in states:
        return states[(p1_pos, p2_pos, p1_score, p2_score)]

    ans = (0,0)
    for r1 in (1,2,3):
        for r2 in (1,2,3):
            for r3 in (1,2,3):
                p1_pos_new = (p1_pos+r1+r2+r3-1) % 10 + 1
                p1_score_new = p1_score + p1_pos_new 

                x1,y1 = count_winners(p2_pos, p1_pos_new, p2_score, p1_score_new)
                ans = (ans[0]+y1, ans[1]+x1)
    
    states[(p1_pos, p2_pos, p1_score, p2_score)] = ans 
    return ans 

part2 = max(count_winners(p1_pos, p2_pos, p1_score, p2_score))


print(part1)
print(part2)



