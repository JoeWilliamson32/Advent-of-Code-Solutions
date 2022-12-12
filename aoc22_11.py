import numpy as np

def data_generator():
    monkeys = []
    for monkey in open('input.txt').read().strip().split('\n\n'):
        lines = monkey.splitlines()
        info = []
        info.append(list(map(int,lines[1].split(":")[1].split(","))))
        info.append(eval("lambda old:" + lines[2].split('=')[1]))
        for line in lines[3:]:
            info.append(int(line.split()[-1]))
        monkeys.append(info)
    
    return monkeys

monkeys = data_generator()
def aoc22_11_part1(monkeys):
    monkeys = data_generator()
    counts = list(np.zeros(len(monkeys)))
    for _ in range(20):
        for i,monkey in enumerate(monkeys):
            while len(monkey[0]) > 0:
                item = monkey[0].pop(0)
                item = monkey[1](item)
                item //= 3
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
                counts[i] += 1

    return np.prod(sorted(counts)[-2:])

def aoc22_11_part2(monkeys):
    monkeys = data_generator()
    mod =1
    for monkey in monkeys:
        mod *= monkey[2]
    counts = list(np.zeros(len(monkeys)))

    for _ in range(10000):
        for i,monkey in enumerate(monkeys):
            while len(monkey[0]) > 0:
                item = monkey[0].pop(0)
                item = monkey[1](item)
                item %= mod
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
                counts[i] += 1

    return np.prod(sorted(counts)[-2:])

part1 = aoc22_11_part1(monkeys)
part2 = aoc22_11_part2(monkeys)

print(part1)
print(part2)