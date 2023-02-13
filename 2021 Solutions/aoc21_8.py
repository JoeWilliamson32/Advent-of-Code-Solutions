from collections import defaultdict

data = open('input.txt').read().strip().splitlines()

# Part 1
count = 0
for line in data:
    _, nums = line.split(' | ')
    signals = nums.split(' ')

    for signal in signals:
        if len(signal) in (2,3,4,7):
            count += 1

part1 = count 

# Part 2 
count = 0
for line in data:
    segments,nums = line.split(' | ')
    segments = segments.split(' ')
    signals = nums.split(' ')
    mapping = defaultdict(int)

    for segment in segments:
        if len(segment) == 2:
            mapping[1] = segment
        if len(segment) == 3:
            mapping[7] = segment
        if len(segment) == 7:
            mapping[8] = segment
        if len(segment) == 4:
            mapping[4] = segment

    for segment in segments:
        if len(segment) == 6:
            value_4 = list(mapping[4])
            value_7 = list(mapping[7])

            if all([char in segment for char in value_4]):
                mapping[9] = segment
            elif all([char in segment for char in value_7]):
                mapping[0] = segment
            else:
                mapping[6] = segment   
    

    for segment in segments:
        if len(segment) == 5:
            value_7 = list(mapping[7])
            value_6 = mapping[6]
            segment_list = list(segment)
            if all([char in segment for char in value_7]):
                mapping[3] = segment
            elif all([char in value_6 for char in segment_list]):
                mapping[5] = segment
            else:
                mapping[2] = segment

    print(signals)
    val = 0 
    for i, signal in enumerate(signals):
        for key, value in mapping.items():
            signal = list(signal)
            if all(char in value for char in signal) and len(value) == len(signal):
                val = (val*10) + int(key)

    count += val

part2 = count


print(part1)
print(part2)