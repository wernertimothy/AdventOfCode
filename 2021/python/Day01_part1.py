
with open('PuzzleInput_day01.txt') as f:
    lines = f.readlines()
    report = [int(line) for line in lines]

increase_count = 0

for i in range(len(report)-1):
    if report[i+1] > report[i] : increase_count = increase_count + 1

print(increase_count)