import pandas as pd
 
df = pd.read_csv('input.csv', header=None)
data = df[0][0]
 
def aoc22_6_part1(data):
    cur_seq = ""
 
    for i in range(len(data)):
        if data[i] not in cur_seq:
            cur_seq += data[i]
 
            if len(cur_seq) == 4:
                return i+1
 
        else:
            pos = cur_seq.index(data[i])
            cur_seq = cur_seq[pos+1:] + data[i]
    
        
def aoc22_6_part2(data):
    cur_seq = ""
 
    for i in range(len(data)):
        if data[i] not in cur_seq:
            cur_seq += data[i]
 
            if len(cur_seq) == 14:
                return i+1
 
        else:
            pos = cur_seq.index(data[i])
            cur_seq = cur_seq[pos+1:] + data[i]
            
 
part1 = aoc22_6_part1(data)
part2 = aoc22_6_part2(data)
 
print(part1)
print(part2)
 