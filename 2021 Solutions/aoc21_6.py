from collections import defaultdict

data = open('input.txt').read().strip()
data = [int(x) for x in data.split(',')]

# Part 1
start_state = defaultdict(int) 
for num in data:
    if num in start_state:
        start_state[num] += 1
    else:
        start_state[num] = 1

for _ in range(80):
    end_state = defaultdict(int)
    for key, value in start_state.items():
        if key == 0:
            end_state[6] += value
            end_state[8] += value
        else:
            end_state[key-1] += value

    start_state = end_state

part1 = sum(end_state.values())


# Part 2
start_state = defaultdict(int) 
for num in data:
    if num in start_state:
        start_state[num] += 1
    else:
        start_state[num] = 1

for _ in range(256):
    end_state = defaultdict(int)
    for key, value in start_state.items():
        if key == 0:
            end_state[6] += value
            end_state[8] += value
        else:
            end_state[key-1] += value

    start_state = end_state

part2 = sum(end_state.values())


print(part1)
print(part2)