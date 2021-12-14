
with open('PuzzleInput_day14.txt') as f:
    lines = f.readlines()
    polymer = lines[0].strip()
    insertion_rules = [line.strip().split(' -> ') for line in lines[2:]]

insertion_rules = {rule[0]:rule[1] for rule in insertion_rules}
elements = []
for pair in insertion_rules:
    if insertion_rules[pair] not in elements:
        elements.append(insertion_rules[pair])

steps = 10
for k in range(steps):
    monomer = list(polymer)
    for l in range(len(polymer)-1):
        monomer.insert(2*l+1,insertion_rules[polymer[l:l+2]])
    polymer = str().join(monomer)

values = []
for element in elements:
    values.append(polymer.count(element))

print(max(values)-min(values))
