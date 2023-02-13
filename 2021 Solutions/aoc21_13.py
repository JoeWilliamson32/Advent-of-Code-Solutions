import pandas as pd
import numpy as np

df_dots = pd.read_csv('problem13_dots.txt', header=None, names=['x', 'y'])
df_folds = pd.read_csv('problem13_folds.txt', header=None)

def buildCoords(df_dots):
    empty = pd.DataFrame(0, index=range(df_dots['y'].max()+1), columns=range(df_dots['x'].max()+1))

    for i in range(len(df_dots)):
        x_coord = df_dots.iloc[i,]['x']
        y_coord = df_dots.iloc[i,]['y']
        empty.iloc[y_coord, x_coord] += 1

    return empty

output = buildCoords(df_dots)
output1 = output.loc[:,656:]
output2 = output.loc[:, :654]
output1 = output1.loc[:, ::-1]
output1.columns = output2.columns
test = output1 + output2
test[test>1] = 1
part1 = test.sum().sum()

def xSplit(df):
    x = (len(df.columns)-1)//2
    df_split1 = df.loc[:,:x-1]
    df_split2 = df.loc[:, x+1:]
    df_split2 = df_split2.loc[:, ::-1]
    df_split2.columns = df_split1.columns
    df_comb = df_split1 + df_split2 
    df_comb[df_comb>1] = 1
    
    return df_comb


def ySplit(df):
    y = (len(df)-1)//2
    df_split1 = df.loc[:y-1,:]
    df_split2 = df.loc[y+1:,:]
    df_split2 = df_split2.loc[::-1, :]
    df_split2.index = df_split1.index
    df_comb = df_split1 + df_split2
    df_comb[df_comb>1] = 1

    return df_comb


test = ySplit(ySplit(ySplit(xSplit(ySplit(xSplit(ySplit(xSplit(ySplit(xSplit(ySplit(xSplit(buildCoords(df_dots)))))))))))))
test[test==1] = '#'
print(test)
