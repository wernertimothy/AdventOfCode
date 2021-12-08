
with open('PuzzleInput_day08.txt') as f:
    notes = f.readlines()
    notes = [[elem.split() for elem in entry.strip().split(' | ')] for entry in notes]

output_sum = 0

for entry in notes:
    configuration = dict.fromkeys([0,1,2,3,4,5,6,7,8,9])
    # get 1,4,7,8
    found_one = False
    found_four = False
    found_seven = False
    found_eight = False
    for digit in entry[0]:
        if len(digit) == 2:
            configuration[1] = digit
            found_one = True
        elif len(digit) == 4:
            configuration[4] = digit
            found_four = True
        elif len(digit) == 3:
            configuration[7] = digit
            found_seven = True
        elif len(digit) == 7:
            configuration[8] = digit
            found_eight = True
        if found_one*found_four*found_seven*found_eight: break
    # get a
    a = configuration[7]
    for char in configuration[1]:
        a = a.replace(char, '')
    # get (0,6,9) and (2,5,3)
    zerosixnine = [elem for elem in entry[0] if len(elem)==6]
    twofivethree = [elem for elem in entry[0] if len(elem)==5]
    # get c, f
    contains = True
    for digit in zerosixnine:
        if configuration[1][0] not in digit:
            contains = False
            break
    f = configuration[1][0] if contains else configuration[1][1]
    c = configuration[1].replace(f,'')
    # get 3
    for digit in twofivethree:
        if c in digit and f in digit:
            configuration[3] = digit
            twofivethree.remove(digit)
            break
    # get 2, 5
    if c in twofivethree[0]:
        configuration[2] = twofivethree[0]
        configuration[5] = twofivethree[1]
    else:
        configuration[2] = twofivethree[1]
        configuration[5] = twofivethree[0]
    twofivethree.clear()
    # get 6
    for digit in zerosixnine:
        if c not in digit:
            configuration[6] = digit
            zerosixnine.remove(digit)
            break
    # get 9, 0
    zeronine = zerosixnine.copy()
    for char in [a, c, f]:
        for k, digit in enumerate(zeronine):
            zeronine[k] = digit.replace(char,'')
    for digit in zerosixnine:
        for char in digit:
            if char in zerosixnine[0] and char in zerosixnine[1]:
                zeronine[0] = zeronine[0].replace(char,'')
                zeronine[1] = zeronine[1].replace(char,'')
    if zeronine[0] in configuration[4]:
        configuration[9] = zerosixnine[0]
        configuration[0] = zerosixnine[1]
    else:
        configuration[9] = zerosixnine[1]
        configuration[0] = zerosixnine[0]
    # get output
    output = ''
    for digit in entry[1]:
        for key, val in configuration.items():
            if sorted(digit) == sorted(val):
                output = output + str(key)

    output_sum = output_sum + int(output)

print(output_sum)