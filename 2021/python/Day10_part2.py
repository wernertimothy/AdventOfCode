
with open('PuzzleInput_day10.txt') as f:
    navigation_subsystem = [line.strip() for line in f.readlines()]

open = ['(','[','{','<']
close = [')',']','}','>']
characters = dict(zip(open,close))
points = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

syntax_error_score = 0
navigation_subsystem_copy = navigation_subsystem.copy()
for line in navigation_subsystem_copy:
    stack = []
    for char in line:
        if char in open:
            stack.append(char)
        elif char in close:
            if characters[stack.pop()] != char:
                navigation_subsystem.remove(line)
        else:
            raise Exception(f"i don't know the character {char}")

scores = []
for line in navigation_subsystem:
    stack = []
    for char in line:
        if char in open:
            stack.append(char)
        if char in close:
            stack.pop()
    completion = ''
    for char in reversed(stack):
        completion = completion + characters[char]
    score = 0
    for char in completion:
        score = score*5 + points[char]
    scores.append(score)

median = int((len(scores)+1)/2-1)
print(sorted(scores)[median])