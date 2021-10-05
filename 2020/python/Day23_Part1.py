
# cups = [3,8,9,1,2,5,4,6,7]
cups = [2,1,5,6,9,4,7,8,3]
num_cups = len(cups)
max_label = max(cups)
min_label = min(cups)

current_cup_idx = 0

for move in range(100):
    # pick up three:
    current_cup = cups[current_cup_idx]
    pick_up = cups[1:4]
    cups = cups[4:] + cups[:1]
    # select destination
    destination_lable = current_cup
    while True:
        destination_lable -= 1
        if destination_lable < min_label:
            destination_lable = max_label
        if not destination_lable in pick_up:
            break
    destination_idx = cups.index(destination_lable)+1
    # place picked cups back 
    cups = cups[:destination_idx] + pick_up + cups[destination_idx:]

one_idx = cups.index(1)
order = cups[one_idx+1:] + cups[:one_idx]
print(order)