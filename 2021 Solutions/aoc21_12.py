from re import L
import pandas as pd
from collections import defaultdict

df = pd.read_csv('problem12.txt', header=None, sep='-', names=['Loc1', 'Loc2'])

# Arrange verticies into a dictionary
def adjVertex(df):
    X = defaultdict()
    for i in range(len(df)):
        if df.iloc[i,0] not in X:
            X[df.iloc[i,0]] = []
        if df.iloc[i,1] not in X:
            X[df.iloc[i,1]] = []
        X[df.iloc[i,0]].append(df.iloc[i,1])
        X[df.iloc[i,1]].append(df.iloc[i,0])
    return X

dict = adjVertex(df)

# Part 1
def pathCount1(input):
    all_paths = set()
    todo = [('start',)]
    while len(todo)>0:
        path = todo.pop()

        if path[-1] == 'end':
            all_paths.add(path)
            continue
        
        for cand in input[path[-1]]:
            if not cand.islower() or cand not in path:
                todo.append((*path, cand))
    return len(all_paths)

# Part 2
def pathCount2(input):
    all_paths = set()
    todo = [(('start',), False)]
    while len(todo)>0:
        path, doubleCave = todo.pop()

        if path[-1] == 'end':
            all_paths.add(path)
            continue
        
        for cand in input[path[-1]]:
            if cand == 'start':
                continue
            elif cand.isupper() or cand not in path:
                todo.append(((*path, cand), doubleCave))
            elif not doubleCave and path.count(cand) == 1:
                todo.append(((*path, cand), True))

    return len(all_paths)

part1 = pathCount1(dict)
part2 = pathCount2(dict)

print(part1)
print(part2)
