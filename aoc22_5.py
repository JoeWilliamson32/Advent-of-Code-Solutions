import pandas as pd

df = pd.read_csv('input.csv', header=None)
df.columns = ['Movements']


df2 = df[9:].reset_index(drop=True)

def aoc22_5_part1(df2):
    # Will come back a write a parser - really cba to do for the time being
    stack1 = ['S', 'M' , 'R', 'N', 'W', 'J' , 'V' , 'T']
    stack2 = ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V']
    stack3 = ['B', 'J', 'F', 'H', 'D', 'R', 'P']
    stack4 = ['F', 'R', 'P', 'B', 'M', 'N', 'D']
    stack5 = ['H', 'V', 'R', 'P', 'T', 'B']
    stack6 = ['C', 'B', 'P', 'T']
    stack7 = ['B', 'J', 'R', 'P', 'L']
    stack8 = ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W']
    stack9 = ['L', 'S', 'G']

    stack_dict = {1:stack1, 
            2:stack2, 
            3:stack3, 
            4:stack4, 
            5:stack5, 
            6:stack6, 
            7:stack7, 
            8:stack8, 
            9:stack9
        }    

    for i in range(len(df2)):
        numbers = df2['Movements'][i].rsplit(' ')[1::2]
        no_moved = int(numbers[0])
        stack_start = int(numbers[1])
        stack_end = int(numbers[2])

        stack_dict[stack_end] += stack_dict[stack_start][-no_moved:][::-1]
        length = len(stack_dict[stack_start])
        stack_dict[stack_start] = stack_dict[stack_start][:length-no_moved]
        
    res = ""
    for value in stack_dict.values():
        res += value[-1]
        
    return res

def aoc22_5_part2(df2):
    # Will come back a write a parser - really cba to do for the time being
    stack1 = ['S', 'M' , 'R', 'N', 'W', 'J' , 'V' , 'T']
    stack2 = ['B', 'W', 'D', 'J', 'Q', 'P', 'C', 'V']
    stack3 = ['B', 'J', 'F', 'H', 'D', 'R', 'P']
    stack4 = ['F', 'R', 'P', 'B', 'M', 'N', 'D']
    stack5 = ['H', 'V', 'R', 'P', 'T', 'B']
    stack6 = ['C', 'B', 'P', 'T']
    stack7 = ['B', 'J', 'R', 'P', 'L']
    stack8 = ['N', 'C', 'S', 'L', 'T', 'Z', 'B', 'W']
    stack9 = ['L', 'S', 'G']

    stack_dict = {1:stack1, 
            2:stack2, 
            3:stack3, 
            4:stack4, 
            5:stack5, 
            6:stack6, 
            7:stack7, 
            8:stack8, 
            9:stack9
        }

    for i in range(len(df2)):
        numbers = df2['Movements'][i].rsplit(' ')[1::2]
        no_moved = int(numbers[0])
        stack_start = int(numbers[1])
        stack_end = int(numbers[2])

        stack_dict[stack_end] += stack_dict[stack_start][-no_moved:]
        length = len(stack_dict[stack_start])
        stack_dict[stack_start] = stack_dict[stack_start][:length-no_moved]
        
    res = ""
    for value in stack_dict.values():
        res += value[-1]
        
    return res

part1 = aoc22_5_part1(df2)
part2 = aoc22_5_part2(df2)

print(part1)
print(part2)