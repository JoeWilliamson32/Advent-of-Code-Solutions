data = open('input.txt').read().strip()
data = [line for line in data.split('\n')]

# Part 1 
grid = [['.' for _ in range(550)] for _ in range(200)]
y_max = 0
x_max = 0
for line in data:
    values = line.split('->')
    for i, coord in enumerate(values):
        
        if i == 0:
            continue
        else:
            x_curr,y_curr = eval(coord)[0], eval(coord)[1]
            x_prev, y_prev = eval(values[i-1])[0], eval(values[i-1])[1]
            
        y_max = max(y_max, y_curr)
        x_max = max(x_max, x_curr)

        if x_curr == x_prev:
            dy = abs(y_curr - y_prev)
            y = min(y_curr, y_prev)
            for j in range(dy+1):
                grid[y+j][x_curr] = '#' 

        elif y_curr == y_prev:
            dx = abs(x_curr - x_prev)
            x = min(x_curr, x_prev)
            for j in range(dx+1):
                grid[y_curr][x+j] = '#' 

count = 0
for _ in range(1000):
    try:
        x,y = 500,0
        while True:
            if grid[y+1][x] == '.':
                y += 1
            elif grid[y+1][x-1] == '.':
                y += 1
                x -= 1
            elif grid[y+1][x+1] == '.':
                y += 1
                x += 1
            else:
                break
        count += 1
        grid[y][x] = 'O'
        
    except IndexError:
        break
    
part1 = count

# Part 2 
grid = [['.' for _ in range(x_max*2)] for _ in range(y_max+3)]
for j in range(len(grid[y_max])):
    grid[y_max+2][j] = '#'
    
y_max = 0
x_max = 0
for line in data:
    values = line.split('->')
    for i, coord in enumerate(values):
        
        if i == 0:
            continue
        else:
            x_curr,y_curr = eval(coord)[0], eval(coord)[1]
            x_prev, y_prev = eval(values[i-1])[0], eval(values[i-1])[1]
            
        y_max = max(y_max, y_curr)
        x_max = max(x_max, x_curr)

        if x_curr == x_prev:
            dy = abs(y_curr - y_prev)
            y = min(y_curr, y_prev)
            for j in range(dy+1):
                grid[y+j][x_curr] = '#' 

        elif y_curr == y_prev:
            dx = abs(x_curr - x_prev)
            x = min(x_curr, x_prev)
            for j in range(dx+1):
                grid[y_curr][x+j] = '#' 
        

count = 0
for i in range(100000):
    x,y = 500,0
    while True:
        if grid[y+1][x] == '.':
            y += 1
        elif grid[y+1][x-1] == '.':
            y += 1
            x -= 1
        elif grid[y+1][x+1] == '.':
            y += 1
            x += 1
        else:
            count += 1
            grid[y][x] = 'O'
            break
  
    if grid[0][500] == 'O':
        break

part2 = count


print(part1)
print(part2)
    
    
        
    
    