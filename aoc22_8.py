import pandas as pd

data = open('input.txt').read()
data = [x for x in data.split('\n')]
data = data[:-1]
df = pd.DataFrame(data)
df.columns = ['flag']
df = df.flag.apply(lambda x: pd.Series(list(x)))
df = df.astype(int)

def aoc22_8_part1(df):
    count = 0
    for i in range(1, len(df)-1):
        for j in range(1, len(df)-1):
            # Top Check
            if int(df.iloc[i,j]) > max([int(i) for i in list(df.iloc[:i, j])]):
                count += 1
            # Bottom Check
            elif int(df.iloc[i,j]) > max([int(i) for i in list(df.iloc[i+1: , j])]):
                count += 1
            # LHS Check
            elif int(df.iloc[i,j]) > max([int(i) for i in list(df.iloc[i, :j])]):
                count += 1
            # RHS Check
            elif int(df.iloc[i,j]) > max([int(i) for i in list(df.iloc[i, j+1:])]):
                count += 1

                
    return count+((len(df)-1)*4)


def aoc22_8_part2(df):
    maxScore = 0
    count = 0
    for i in range(len(df)):
        for j in range(len(df)):
            curVal = df.iloc[i,j]
            
            # Top Check
            top_score = 0
            for num in df.iloc[:i, j][::-1]:
                if curVal > num:
                    top_score += 1
                else:
                    break
            if top_score < len(df.iloc[:i, j]):
                top_score += 1

                    
            bottom_score = 0
            for num in df.iloc[i+1:,j]:
                if curVal > num:
                    bottom_score += 1
                else:
                    break
            if bottom_score < len(df.iloc[i+1:,j]):
                bottom_score += 1
                
                    
            left_score = 0
            for num in df.iloc[i,:j][::-1]:
                if curVal > num:
                    left_score += 1
                else:
                    break 
            if left_score < len(df.iloc[i,:j]):
                left_score += 1
                
                
            right_score = 0
            for num in df.iloc[i,j+1:]:
                if curVal > num:
                    right_score += 1
                else:
                    break
            if right_score < len(df.iloc[i,j+1:]):
                right_score += 1
                
            totalScore = top_score*bottom_score*left_score*right_score
            
            maxScore = max(maxScore, totalScore)

                
    return maxScore


part1 = aoc22_8_part1(df)
part2 = aoc22_8_part2(df)

print(part1, part2)