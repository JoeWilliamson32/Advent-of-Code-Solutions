import pandas as pd
import numpy as np

df = pd.read_csv('problem1.txt', header=None)
df = df.squeeze()

# Part 1
part1 = sum([((df[i+1] > df[i]).astype(int)) for i in range(len(df)-1)])
part1_alt = df.diff().gt(0).sum()

# Part 2 
part2 = np.sum([(np.sum(df[i+1:i+4])>np.sum(df[i:i+3])).astype(int) for i in range(len(df))])
part2_alt = df.diff(3).gt(0).sum()


print(part1)
print(part2)
