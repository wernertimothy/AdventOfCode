
with open('PuzzleInput_day08.txt') as f:
    notes = f.readlines()
    notes = [[elem.split() for elem in entry.strip().split(' | ')] for entry in notes]

easy_digit_lens = [2,3,4,7]

counter = 0
for entry in notes:
    easy_digits = [elem for elem in entry[0] if len(elem) in easy_digit_lens]
    easy_digits = {len(digit): digit for digit in easy_digits}
    for elem in entry[1]:
        if len(elem) in easy_digit_lens:
            unique = True
            for char in elem:
                if char not in easy_digits[len(elem)]:
                    unique = False
                    break
            if unique: counter = counter + 1

print(counter)