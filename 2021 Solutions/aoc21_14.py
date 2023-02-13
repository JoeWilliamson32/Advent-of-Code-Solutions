import pandas as pd
import collections
from collections import defaultdict

df_string = pd.read_csv('problem14_template.txt', header=None)
df_table = pd.read_csv('problem14_pairrules.txt', header=None, sep='->', names=['input', 'string'])

df_string  = str(df_string).replace(' ', '')[3:]
df_table['input'] = df_table['input'].str.strip()
df_table['string'] = df_table['string'].str.strip()

#  Part 1 
def strMaker(df_table, df_string):
    df_stringMod = (df_string + '.')[:-1]
    df_stringMod = list(df_stringMod)
    for i in range(len(df_string)-1):
        pair = df_string[i:i+2]
        x = df_table[df_table['input'] == pair]['string'].item()
        df_stringMod.insert(1+(2*i), x)
    
    df_stringMod = ''.join(df_stringMod)
    return df_stringMod

finalList = strMaker(df_table, strMaker(df_table, strMaker(df_table, strMaker(df_table, strMaker(df_table, strMaker(df_table, strMaker(df_table, strMaker(df_table, strMaker(df_table, strMaker(df_table, df_string))))))))))
counter = collections.Counter(finalList)
part1 = counter[max(counter, key=counter.get)] - counter[min(counter, key=counter.get)]

 
#  Part 2 
def dictMaker(df_string):
    X = defaultdict()
    for i in range(len(df_string)-1):
        pair = df_string[i:i+2]
        if pair not in X:
            X[pair] = 0
        X[pair] += 1
    return X

def dictCounter(df_table, df_string):
    X = dictMaker(df_string)
    for i in range(40):
        Y = defaultdict()

        for key, cnt in X.items():
            match = df_table[df_table['input'] == key]['string'].item()
            key1 = key[0] + match
            key2 = match + key[1]

            if key1 not in Y:
                Y[key1] = 0 
            Y[key1] += cnt

            if key2 not in Y:
                Y[key2] = 0
            Y[key2] += cnt

        X = Y
        i += 1

    return Y

def elementCounter(dict):
    X = defaultdict()

    for key, cnt in dict.items():
        key0 = key[0]
        key1 = key[1]

        if key0 not in X:
            X[key0] = 0
        X[key0] += cnt/2
    
        if key1 not in X:
            X[key1] = 0 
        X[key1] += cnt/2
    
    return X

x = elementCounter(dictCounter(df_table, df_string))
part2 = x[max(x, key=x.get)] - x[min(x, key=x.get)]-1


print(part1)
print(part2)
