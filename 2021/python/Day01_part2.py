
with open('PuzzleInput_day01.txt') as f:
    lines = f.readlines()
    report = [int(line) for line in lines]

increase_count = 0
window_size = 3

for i in range(len(report)-window_size):
    if report[i+window_size] > report[i] : increase_count = increase_count + 1

print(increase_count)