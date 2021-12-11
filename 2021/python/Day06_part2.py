
values = [i for i in range(9)]
numbers = [0 for i in range(9)]
count = dict(zip(values,numbers))

with open('PuzzleInput_day06.txt') as f:
    data = f.readlines()
    for timer in data[0].split(','):
        count[int(timer)] += 1

days = 256
for day in range(days):
    tmp = count[1]
    count[7], count[6], count[5], count[4], count[3], count[2], count[1] = count[8], count[7], count[6], count[5], count[4], count[3], count[2]
    count[8] = count[0]
    count[6] += count[0]
    count[0] = tmp

total = 0
for value in count:
    total += count[value]

print(total)