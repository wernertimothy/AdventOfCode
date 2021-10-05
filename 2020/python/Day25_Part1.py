
def bruteforce_loopsize(subject_number, key):
    value = 1
    loop_size = 0
    while True:
        loop_size += 1
        value *= subject_number
        value %= 20201227
        if value == key: break
    return loop_size

subject_number = 7
card_pk = 3248366
door_pk = 4738476

card_loop_size = bruteforce_loopsize(subject_number, card_pk)
door_loop_size = bruteforce_loopsize(subject_number, door_pk)

# print(card_loop_size)
# print(door_loop_size)

value = 1
for _ in range(card_loop_size):
    value *= door_pk
    value %= 20201227

print(value)