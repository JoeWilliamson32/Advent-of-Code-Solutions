import pandas as pd

df = pd.read_csv('input.csv', header=None)
df.columns = ['A', 'B']

def aoc22_4_part1(df):
    count = 0
    for i in range(len(df)):
        lower_bound_A, upper_bound_A = int(df['A'][i].rsplit('-')[0]), int(df['A'][i].rsplit('-')[1])
        lower_bound_B, upper_bound_B = int(df['B'][i].rsplit('-')[0]), int(df['B'][i].rsplit('-')[1])
        
        if lower_bound_A >= lower_bound_B and upper_bound_A <= upper_bound_B:
            count += 1 
            
#       Needs to be elif otherwise we'll be double counting instances where both are true - i.e. where A=B
        elif lower_bound_B >= lower_bound_A and upper_bound_B <= upper_bound_A:
            count += 1 
            
    return count
            

def aoc22_4_part2(df):
    count = 0
    for i in range(len(df)):
        lower_bound_A, upper_bound_A = int(df['A'][i].rsplit('-')[0]), int(df['A'][i].rsplit('-')[1])
        lower_bound_B, upper_bound_B = int(df['B'][i].rsplit('-')[0]), int(df['B'][i].rsplit('-')[1])
        
        if lower_bound_A > upper_bound_B:
            count += 1
            
        elif upper_bound_A < lower_bound_B:
            count += 1
            
        elif lower_bound_B > upper_bound_A:
            count += 1
            
        elif upper_bound_B < lower_bound_A:
            count += 1
            
    return len(df)-count
            


part1 = aoc22_4_part1(df)
part2 = aoc22_4_part2(df)

print(part1)
print(part2)
