import pandas as pd
from collections import defaultdict

df = pd.read_csv('input.csv', header=None)
df.columns = ['Command']

def aoc22_7_part1(df):
    directories = defaultdict(int)
    path  = []

    for i in range(len(df)):
        commands = df['Command'][i].rsplit(' ')

        if commands[1] == 'cd':
            if commands[2] == '..':
                path.pop()
            else:    
                path.append(commands[2])

        elif commands[1] == 'ls':
            continue

        elif commands[0] == 'dir':
            continue

        else:
            size = int(commands[0])
            for j in range(1,len(path)+1):
                directories['/'.join(path[:j])] += size


    ans = 0
    for key, value in directories.items():
        if value < 100000:
            ans += value 
        
    return ans
       
        
def aoc22_7_part2(df):
    directories = defaultdict(int)
    path  = []

    for i in range(len(df)):
        commands = df['Command'][i].rsplit(' ')

        if commands[1] == 'cd':
            if commands[2] == '..':
                path.pop()
            else:    
                path.append(commands[2])

        elif commands[1] == 'ls':
            continue

        elif commands[0] == 'dir':
            continue

        else:
            size = int(commands[0])
            for j in range(1,len(path)+1):
                directories['/'.join(path[:j])] += size
                
    used_space = directories['/']
    free_space = 70000000 - used_space 
    size_to_delete = 30000000 - free_space
    size_to_delete

    minSum = used_space
    for key, value in directories.items():
        if value > size_to_delete:
            minSum = min(minSum, value)
            
            
    return minSum

part1 = aoc22_7_part1(df)
part2 = aoc22_7_part2(df)

print(part1)
print(part2)

