from collections import defaultdict

data = open('input.txt').read().split()

snafu = {"=":-2, "-":-1, "0":0, "1":1, "2":2}

totalSum = 0
for line in data:
    curSum = 0
    for i in range(len(line)):
        power = 5**(len(line)-1-i)
        num = snafu[line[i]]
        curSum += (power*num)
    totalSum += curSum
totalSum

ans = ""
while totalSum:
    rem = totalSum % 5
    totalSum //= 5
    
    if rem <= 2:
        ans = str(rem) + ans
    else:
        ans = "   =-"[rem] + ans
        totalSum += 1


part1 = ans
print(part1)
