import pandas as pd

df = pd.read_csv('input.csv', header=None, sep=' ')
df.columns = ['Opp', 'Us']

def score_calc1(df):
    score = 0
    
    for i in range(len(df)):
        if df['Us'][i] == 'X':
            score += 1
            
            if df['Opp'][i] == 'C':
                score += 6 
                
            elif df['Opp'][i] == 'B':
                score += 0 
                
            elif df['Opp'][i] == 'A':
                score += 3
                
        elif df['Us'][i] == 'Y':
            score += 2
            
            if df['Opp'][i] == 'C':
                score += 0
                
            elif df['Opp'][i] == 'B':
                score += 3
                
            elif df['Opp'][i] == 'A':
                score += 6
                
        elif df['Us'][i] == 'Z':
            score += 3
            
            if df['Opp'][i] == 'C':
                score += 3
                
            elif df['Opp'][i] == 'B':
                score += 6
                
            elif df['Opp'][i] == 'A':
                score += 0
                
    return score
                
                

def score_calc2(df):
    score = 0
    
    for i in range(len(df)):
        if df['Us'][i] == 'X':
            score += 0
            
            if df['Opp'][i] == 'C':
#           Scissors beats paper - so if they pick scissors and we need to lose, we pick paper and add 2 to score
#           And so on for other examples
                score += 2
                
            elif df['Opp'][i] == 'B':
                score += 1
                
            elif df['Opp'][i] == 'A':
                score += 3
                
        elif df['Us'][i] == 'Y':
            score += 3
            
            if df['Opp'][i] == 'C':
                score += 3
                
            elif df['Opp'][i] == 'B':
                score += 2
                
            elif df['Opp'][i] == 'A':
                score += 1
                
        elif df['Us'][i] == 'Z':
            score += 6
            
            if df['Opp'][i] == 'C':
                score += 1
                
            elif df['Opp'][i] == 'B':
                score += 3
                
            elif df['Opp'][i] == 'A':
                score += 2
                
    return score
                
                
part_1 = score_calc1(df)
part_2 = score_calc2(df)

print(part_1)
print(part_2)