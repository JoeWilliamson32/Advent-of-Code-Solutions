from collections import defaultdict

data = open('input.txt').read()
data = [x for x in data.split('\n')]

def aoc22_10_part1(data):
    xSum = 1
    entry = 0
    running_score = defaultdict(int)
    for i in range(len(data)):
        command = data[i].rsplit(' ')[0]

        if command == 'addx':
            cycle = int(data[i].rsplit(' ')[1])

            running_score[entry+1] = xSum * (entry+1)
            entry += 1
            running_score[entry+1] = xSum * (entry+1)
            xSum += cycle
            entry += 1

        else:
            running_score[entry+1] = xSum * (entry+1)
            entry += 1
            
    return running_score[20]+running_score[60]+running_score[100]+running_score[140]+running_score[180]+running_score[220]



def aoc22_10_part2(data):
    xSum = 1
    entry = 0
    running_score = defaultdict(int)
    for i in range(len(data)):
        command = data[i].rsplit(' ')[0]

        if command == 'addx':
            cycle = int(data[i].rsplit(' ')[1])

            running_score[entry] = xSum 
            entry += 1
            running_score[entry] = xSum
            xSum += cycle
            entry += 1

        else:
            running_score[entry] = xSum 
            entry += 1

    row1 = ['.']*40
    row2 = ['.']*40
    row3 = ['.']*40
    row4 = ['.']*40
    row5 = ['.']*40
    row6 = ['.']*40
    for key, value in running_score.items():
        if key < 40:
            if key in range(value-1, value+2):
                 row1[key] = '#'
        if key >= 40 and key < 80:
            if key - 40 in range(value-1, value+2):
                row2[key-40] = '#'
        if key >= 80 and key < 120:
            if key - 80 in range(value-1, value+2):
                row3[key-80] = '#'
        if key >= 120 and key < 160:
            if key - 120 in range(value-1, value+2):
                row4[key-120] = '#'
        if key >= 160 and key < 200:
            if key - 160 in range(value-1, value+2):
                row5[key-160] = '#'
        if key >= 200 and key < 240:
            if key - 200 in range(value-1, value+2):
                row6[key-200] = '#'
                
    for x in row1:
        print(x, end='')
    print('')
    for x in row2:
        print(x, end='')
    print('')
    for x in row3:
        print(x, end='')
    print('')
    for x in row4:
        print(x, end='')
    print('')
    for x in row5:
        print(x, end='')
    print('')
    for x in row6:
        print(x, end='')


print(aoc22_10_part1(data))
aoc22_10_part2(data)