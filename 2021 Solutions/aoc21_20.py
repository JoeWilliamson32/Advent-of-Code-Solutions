data = open('input.txt').read().strip()
alg, data = data.split('\n\n')

data = [x for x in data.split('\n')]
pixels = set()
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == '#':
            pixels.add((r,c))


def flash(pixels, on):
    minR = min([r for r,c in pixels])
    maxR = max([r for r,c in pixels])
    minC = min([c for r,c in pixels])
    maxC = max([c for r,c in pixels])

    new_pixels = set()
    for r in range(minR-10,maxR+10):
        for c in range(minC-10,maxC+10):
            num = ''
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    nr = r + dr 
                    nc = c + dc 

                    if ((nr, nc) in pixels) == on:
                        num = num + '1'
                    else:
                        num = num + '0'

            idx = int(num, 2)
            conv = alg[idx]

            if (conv == '#') != on:
                new_pixels.add((r,c))

    return new_pixels

for t in range(50):
  if t==2:
    part1 = len(pixels)
  pixels = flash(pixels, t%2==0)
part2 = len(pixels)


print(part1)
print(part2)

