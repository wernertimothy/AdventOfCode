
with open('PuzzleInput_day06.txt') as f:
    data = f.readlines()
    timers = [int(timer) for timer in data[0].split(',')]

days = 80
for day in range(days):
    new_timer = []
    for i in range(len(timers)):
        if timers[i] == 0:
            new_timer.append(8)
            timers[i] = 6
        else:
            timers[i] = timers[i]-1
    for new in new_timer: timers.append(new)
    # print([fish._internal_timer for fish in lanternfishs])

print(len(timers))