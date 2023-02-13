from collections import defaultdict

data = open('input.txt').read().strip().splitlines()

# Part 1 
zero_count = defaultdict(int)
one_count = defaultdict(int)

for line in data:
    for i in range(len(line)):
        if line[i] == '0':
            zero_count[i] += 1
        else:
            one_count[i] += 1

gamma = []
epsilon = []
for key in sorted(zero_count):
    if zero_count[key] > one_count[key]:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

gamma_num = 0
for i in range(len(gamma)):
    if gamma[i] == '1':
        gamma_num += 2**(len(gamma)-1-i)

epsilon_num = 0
for i in range(len(epsilon)):
    if epsilon[i] == '1':
        epsilon_num += 2**(len(epsilon)-1-i)

part1 = gamma_num * epsilon_num


# Part 2 
ogr = data[:]
i = 0
while len(ogr) > 1:
    zero_idx = []
    one_idx =[]

    for row, line in enumerate(ogr):
        cur_bit = line[i]
        if cur_bit == '0':
            zero_idx.append(row)
        else:
            one_idx.append(row)

    if len(one_idx) >= len(zero_idx):
        ogr = [ogr[j] for j in one_idx]

    else:
        ogr = [ogr[j] for j in zero_idx]

    i+=1

co2sr = data[:]
i=0
while len(co2sr) > 1:
    zero_idx = []
    one_idx =[]

    for row, line in enumerate(co2sr):
        cur_bit = line[i]
        if cur_bit == '0':
            zero_idx.append(row)
        else:
            one_idx.append(row)

    if len(one_idx) < len(zero_idx):
        co2sr = [co2sr[j] for j in one_idx]

    else:
        co2sr = [co2sr[j] for j in zero_idx]

    i+=1

ogr = ogr[0]
ogr_num = 0
for i in range(len(ogr)):
    if ogr[i] == '1':
        ogr_num += 2**(len(ogr)-1-i)

co2sr = co2sr[0]
co2sr_num = 0
for i in range(len(co2sr)):
    if co2sr[i] == '1':
        co2sr_num += 2**(len(co2sr)-1-i)

part2 = ogr_num * co2sr_num


print(part1)
print(part2)
