data = open('input.txt').read().strip()
data = [line for line in data.split('\n')]

coords = []
for line in data:
    x_signal = int(line.split(' ')[2].split(',')[0].split('=')[1])
    y_signal = int(line.split(' ')[3].split(':')[0].split('=')[1])
    x_beacon = int(line.split(' ')[-2].split(',')[0].split('=')[1])
    y_beacon = int(line.split(' ')[-1].split('=')[1])
    coords.append([(x_signal, y_signal), (x_beacon, y_beacon)])

signals = []
beacons = []
for a,b in coords:
    x1,y1 = a
    x2,y2 = b
    signals.append((x1,y1))
    beacons.append((x2, y2))

# Part 1 - pretty inefficient, had to think of a better way for Part 2 using intervals
positions = set()
for signal, beacon in coords:
    x_signal, y_signal = signal
    x_beacon, y_beacon = beacon
    dist = abs(x_signal - x_beacon) + abs(y_signal - y_beacon)
    
    for i in range(x_signal-dist, x_signal+dist+1):
        j = 2000000
        if (i,j) not in beacons and (i,j) not in signals and (i,j) not in positions:
                dist2 = abs(x_signal - i) + abs(y_signal - j)
                if dist2 <= dist:
                    positions.add((i,j))
                    
part1 = len(positions)
print(part1)


# Part 2
Y_max = 4000000

for Y in range(Y_max+1):
    intervals = []
    for signal, beacon in coords:
        x_signal, y_signal = signal
        x_beacon, y_beacon = beacon
        dist = abs(x_signal - x_beacon) + abs(y_signal - y_beacon)
        dx = dist - abs(y_signal - Y)

        if dx < 0:
            continue

        intervals.append((x_signal-dx, x_signal+dx))

    intervals.sort()

    intervals_merged = []

    for low, high in intervals:
        if not intervals_merged:
            intervals_merged.append([low, high])
            continue

        low_prev, high_prev = intervals_merged[-1]

        if low > high_prev + 1:
            intervals_merged.append([low, high])
            continue
        
        intervals_merged[-1][1] = max(high_prev, high)
    
    x = 0
    for low, high in intervals_merged:
        if x < low:
            print(x * 4000000 + Y)
            exit(0)
        x = max(x, high + 1)
        if x > Y_max:
            break
