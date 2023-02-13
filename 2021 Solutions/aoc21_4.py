import pandas as pd

# Part1 
nums = pd.read_csv('input1.txt', header=None)
boards = pd.read_csv('input2.txt', header=None, delim_whitespace=True)
boards.index = boards.index//5
nums = nums.squeeze()

for num in nums:
    boards = boards.mask(boards == num, 0)
    horz = boards.sum(axis=1).eq(0)[lambda x:x]
    vert = boards.groupby(boards.index).sum().eq(0).any(axis=1)[lambda x: x]
    winners = horz.index.union(vert.index)
    if len(winners)>0:
        break 

part1 = boards.loc[winners].sum().sum()*num

# Part 2 
nums = pd.read_csv('input1.txt', header=None)
boards = pd.read_csv('input2.txt', header=None, delim_whitespace=True)
boards.index = boards.index//5
nums = nums.squeeze()

for num in nums:
    boards = boards.mask(boards == num)
    is_bingo = boards.isna()
    horiz = is_bingo.all(axis=1)[lambda x: x]
    vert = is_bingo.groupby(level=0).all().any(axis=1)[lambda x: x]
    winners = horiz.index.union(vert.index)
    if len(boards) == 5:
        total = boards.stack().sum() * num  
    boards = boards[~boards.index.isin(winners)]
    if len(boards) == 0:
        break

part2 = total


print(part1)
print(part2)

    


        