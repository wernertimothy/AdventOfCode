
with open('PuzzleInput_day07.txt') as f:
    data = f.readlines()[0].strip().split(',')
    positions = [int(pos) for pos in data]

the_cost = None
min_pos = min(positions)
max_pos = max(positions)

the_cost = None
the_pos = None

for this_pos in range(max_pos-min_pos+1):
    this_cost = 0
    for crab_pos in positions:
        this_cost = this_cost + abs(crab_pos - this_pos)
    if the_cost is None:
        the_pos = this_pos
        the_cost = this_cost
    else: 
        if this_cost < the_cost:
            the_pos = this_pos
            the_cost = this_cost

print(the_cost)
print(the_pos)
