import pandas as pd
import numpy as np


df = pd.read_csv('problem9.txt', 
                 header=None)

df = df.astype(str)
df = df[0].str.split('', expand=True)
df.drop(0,1, inplace=True)
df.drop(101,1, inplace=True)
df = df.astype(int)

# Part 1

low_points = []
for i in range(len(df)):
    
    for j in range(len(df.columns)):
        
        if i == j == 0:
            if df.iloc[i,j] < df.iloc[i+1, j] and df.iloc[i,j] < df.iloc[i, j+1]:
                low_points.append(df.iloc[i,j])
        
        elif i == 0 and j !=0 and j != 99:
            if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i, j+1] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append(df.iloc[i,j])
                
        elif i == 0 and j == 99:
            if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append(df.iloc[i,j])
                
        elif i != 0  and i != 99 and j == 0:
            if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i-1, j] and df.iloc[i,j] < df.iloc[i, j+1]:
                low_points.append(df.iloc[i,j])
                
        elif i != 0 and i != 99 and j == 99:
             if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i-1, j] and df.iloc[i,j] < df.iloc[i, j-1]:
                 low_points.append(df.iloc[i,j])
                 
        elif i == 99 and j == 0:
             if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j+1]:
                low_points.append(df.iloc[i,j])

        elif i == 99 and j != 0 and j != 99:
            if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j+1] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append(df.iloc[i,j])
                
        elif i == 99 and j == 99:
              if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append(df.iloc[i,j])
            
        else:
            if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j+1] and df.iloc[i,j] < df.iloc[i, j-1] and df.iloc[i,j] < df.iloc[i+1,j]:
                low_points.append(df.iloc[i,j])
                

ans = np.sum(low_points) + len(low_points)
part1 = ans

# Part 2

low_points = []
for i in range(len(df)):
    
    for j in range(len(df.columns)):
        
        if i == j == 0:
            if df.iloc[i,j] < df.iloc[i+1, j] and df.iloc[i,j] < df.iloc[i, j+1]:
                low_points.append([i,j])
        
        elif i == 0 and j !=0 and j != 99:
            if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i, j+1] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append([i,j])
                
        elif i == 0 and j == 99:
            if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append([i,j])
                
        elif i != 0  and i != 99 and j == 0:
            if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i-1, j] and df.iloc[i,j] < df.iloc[i, j+1]:
                low_points.append([i,j])
                
        elif i != 0 and i != 99 and j == 99:
             if df.iloc[i,j] < df.iloc[i+1,j] and df.iloc[i,j] < df.iloc[i-1, j] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append([i,j])
                 
        elif i == 99 and j == 0:
             if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j+1]:
                low_points.append([i,j])
                
        elif i == 99 and j != 0 and j != 99:
            if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j+1] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append([i,j])
                
        elif i == 99 and j == 99:
              if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j-1]:
                low_points.append([i,j])
                
        else:
            if df.iloc[i,j] < df.iloc[i-1,j] and df.iloc[i,j] < df.iloc[i, j+1] and df.iloc[i,j] < df.iloc[i, j-1] and df.iloc[i,j] < df.iloc[i+1,j]:
                low_points.append([i,j])                      
        
                
def checkPoint(y, x, df):
    size = 0
    bottomEdge = len(df)
    rightEdge = len(df.columns)
    
    if df.iloc[x,y] == '.' or df.iloc[x,y] == 9:
        return size
    
    df.iloc[x,y] = '.'
    size += 1

    if y+1 < bottomEdge:
        size += checkPoint(y+1, x, df)
    
    if y-1 >= 0:
        size += checkPoint(y-1, x, df)
        
    if x+1 < rightEdge:
        size+= checkPoint(y, x+1, df)
        
    if x-1 >= 0:
        size += checkPoint(y, x-1, df)
        
    return size
                
                
def findBasin(low_points, df):
    sizes = []
    for low in low_points:
        sizes.append(checkPoint(low[0], low[1], df))
        
    return sizes 

part2 = np.product(sorted(findBasin(low_points, df))[-3:])



print(part1)
print(part2)
                
                
                
                
                
                
                
                
