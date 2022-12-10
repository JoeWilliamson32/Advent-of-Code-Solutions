# Just for Part 1 at the minute, come back and do Part 2
import pandas as pd

df = pd.read_csv('input.csv', header=None)
df.columns = ['Movements']

ups = 0
downs = 0
lefts = 0 
rights = 0

for i in range(len(df)):
    pos = df['Movements'][i].rsplit(' ')[0]
    movements = df['Movements'][i].rsplit(' ')[1]
    
    if pos == 'R':
        rights += int(movements)
        
    if pos == 'L':
        lefts += int(movements)
        
    if pos == 'U':
        ups += int(movements)
        
    if pos == 'D':
        downs += int(movements)
    

grid = pd.DataFrame(0, index=range(max(lefts, rights)), columns=range(max(ups, downs)))
x = len(grid.columns)//2
y = len(grid)//2
head_pos_x = x
head_pos_y = y
tail_pos_x = x
tail_pos_y = y

for i in range(len(df)):
    pos = df['Movements'][i].rsplit(' ')[0]
    movements = int(df['Movements'][i].rsplit(' ')[1])
    for j in range(movements):
        if pos == 'L':
            head_pos_x -=1
            if (tail_pos_x - head_pos_x == 2) and (head_pos_y == tail_pos_y):
                tail_pos_x -= 1 
            elif (abs(head_pos_y - tail_pos_y)>1 and abs(head_pos_x - tail_pos_x)>=1) or (abs(head_pos_y - tail_pos_y)>=1 
                                                                                          and abs(head_pos_x - tail_pos_x)>1):
                tail_pos_x = head_pos_x + 1
                tail_pos_y = head_pos_y
            else:
                continue


        if pos == 'D':
            head_pos_y += 1

            if (head_pos_y - tail_pos_y == 2) and (head_pos_x == tail_pos_x):
                tail_pos_y += 1 
            elif (abs(head_pos_y - tail_pos_y)>1 and abs(head_pos_x - tail_pos_x)>=1) or (abs(head_pos_y - tail_pos_y)>=1 
                                                                                          and abs(head_pos_x - tail_pos_x)>1):
                tail_pos_x = head_pos_x 
                tail_pos_y = head_pos_y -1
            else:
                continue

        if pos == 'R':
            head_pos_x += 1

            if (head_pos_x - tail_pos_x == 2) and (head_pos_y == tail_pos_y):
                tail_pos_x += 1 
            elif (abs(head_pos_y - tail_pos_y)>1 and abs(head_pos_x - tail_pos_x)>=1) or (abs(head_pos_y - tail_pos_y)>=1 
                                                                                          and abs(head_pos_x - tail_pos_x)>1):
                tail_pos_x = head_pos_x - 1
                tail_pos_y = head_pos_y 
            else:
                continue

        if pos == 'U':
            head_pos_y -= 1

            if (tail_pos_y - head_pos_y == 2) and (head_pos_x == tail_pos_x):
                tail_pos_y -= 1 
            elif (abs(head_pos_y - tail_pos_y)>1 and abs(head_pos_x - tail_pos_x)>=1) or (abs(head_pos_y - tail_pos_y)>=1 
                                                                                          and abs(head_pos_x - tail_pos_x)>1):
                tail_pos_x = head_pos_x 
                tail_pos_y = head_pos_y +1
            else:
                continue


        if grid.iloc[tail_pos_y, tail_pos_x] == 0:
            grid.iloc[tail_pos_y, tail_pos_x] = 1


part_1 = grid.sum().sum()

print(part_1)