
with open('PuzzleInput_day10.txt') as f:
    navigation_subsystem = [line.strip() for line in f.readlines()]

open = ['(','[','{','<']
close = [')',']','}','>']
characters = dict(zip(open,close))
points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

syntax_error_score = 0
corrupted_lines = []
error_msg = []
for line in navigation_subsystem:
    stack = []
    for char in line:
        if char in open:
            stack.append(char)
        elif char in close:
            expected = characters[stack.pop()]
            if expected != char:
                corrupted_lines.append(line)
                error_msg.append(
                    f'Expected {expected}, but found {char} instead.'
                )
                syntax_error_score = syntax_error_score + points[char]
        else:
            raise Exception(f"i don't know the character {char}")

print(syntax_error_score)