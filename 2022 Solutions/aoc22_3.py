import string
import pandas as pd

df = pd.read_csv('input.csv', header=None)
df.columns = ['String']

lower_case_score = dict(zip(string.ascii_lowercase, range(1,27)))
upper_case_score = dict(zip(string.ascii_uppercase, range(27,53)))
scoring = lower_case_score.copy()
scoring.update(upper_case_score)

def aoc22_3_part1(df):
    score = 0
    for i in range(len(df)):
        mid = len(df['String'][i])//2
        first_half = df['String'][i][:mid]
        second_half = df['String'][i][mid:]
        
        matching = set(first_half).intersection(set(second_half))
        matching = next(iter(matching))
        
        score += scoring[matching]
        
    return score

def aoc22_3_part2(df):
    score = 0
    for i in range(0, len(df), 3):
        str1 = df['String'][i]
        str2 = df['String'][i+1]
        str3 = df['String'][i+2]
    
        matching = set(str1).intersection(set(str2)).intersection(set(str3))
        matching = next(iter(matching))

        score += scoring[matching]

    return score

part1 = aoc22_3_part1(df)
part2 = aoc22_3_part2(df)

print(part1)
print(part2)
