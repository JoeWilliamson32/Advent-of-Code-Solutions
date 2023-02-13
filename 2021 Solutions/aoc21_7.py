import pandas as pd

df = pd.read_csv('problem7.txt', header=None)
df = df.squeeze()

# Part 1
x = []
for num in range(max(df)):
    x.append(abs(num - df).sum())
fuel_exp = min(x)
part1 = fuel_exp

# Part 2
x = []
for num in range(max(df)):
    x.append((abs(num-df)*(abs(num-df)+1)/2).sum())
fuel_exp = min(x)
part2 = fuel_exp


print(part1)
print(part2)