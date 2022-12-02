import pandas as pd

df = pd.read_csv('input.csv', header=None, skip_blank_lines=False).fillna('-').reset_index(drop=True)

calories = list(df[0])

def aoc1_part1(calories):
    maxSum = 0
    curSum = 0
    
    for num in calories:
        if num == '-':
            maxSum = max(curSum, maxSum)
            curSum = 0
        else:
            curSum += num
            
    return maxSum


def aoc1_part2(calories):
    maxSum1 = 0
    maxSum2 = 0
    maxSum3 = 0
    curSum = 0
    for num in calories:
        if num == '-':
            if curSum > maxSum1:
                maxSum3 = maxSum2
                maxSum2 = maxSum1
                maxSum1 = curSum
            elif curSum > maxSum2:
                maxSum3 = maxSum2
                maxSum2 = curSum
            elif curSum > maxSum3:
                maxSum3 = curSum
            curSum = 0
        else:
            curSum += num
            
    return maxSum1+maxSum2+maxSum3

ans_part1 = aoc1_part1(calories)
ans_part2 = aoc1_part2(calories)

print(ans_part1)
print(ans_part2)