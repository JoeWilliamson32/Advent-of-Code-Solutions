from tqdm import tqdm

data = open('input.txt').read().strip()

x,y = data.split(': ')[1].split(',')
xmin, xmax = x.split('=')[1].split('..')
ymin, ymax = y.split('=')[1].split('..')


# Part 1 
xmin = int(xmin)
xmax = int(xmax)
ymax = int(ymax)
ymin = int(ymin)

# Not exactly efficient - but know x can't be greater than max target x value, then just as liberal as possible 
overall_max = 0
for i in tqdm(range(125)):
    for j in range(500):
        x,y = (0,0)
        v_x, v_y = (i,j)
        hit = False
        yMax = 0

        while x <= xmax and y >= ymin:
            x += v_x
            y += v_y
            v_x = max(v_x-1, 0)
            v_y -= 1
            yMax = max(y, yMax)

            if x in range(xmin, xmax+1) and y in range(ymin, ymax+1):
                hit = True 
                overall_max = max(overall_max, yMax)
                break


part1 = overall_max


# Part 2 
count = 0
for i in tqdm(range(126)):
    for j in range(-500,500):
        x,y = (0,0)
        v_x, v_y = (i,j)
        v_xstart = v_x
        v_ystart = v_y
        hit = False

        while x <= xmax and y >= ymin:
            x += v_x
            y += v_y
            v_x = max(v_x-1, 0)
            v_y -= 1

            if x in range(xmin, xmax+1) and y in range(ymin, ymax+1):
                hit = True 
                count += 1
                break


part2 = count


print(part1)
print(part2)