
cave_system = {}
with open('PuzzleInput_day12.txt') as f:
    lines = [line.strip().split('-') for line in f.readlines()]
    for line in lines:
        if line[0] in cave_system:
            cave_system[line[0]].append(line[1])
        else:
            cave_system[line[0]] = [line[1]]
        if line[1] in cave_system:
            cave_system[line[1]].append(line[0])
        else:
            cave_system[line[1]] = [line[0]]

found_paths = []
open_paths = []
for first in cave_system['start']:
    open_paths.append(['start', first])

while open_paths:
    path = open_paths.pop()
    for cave in cave_system[path[-1]]:
        if cave == 'start':
            continue
        elif cave == 'end':
            new_path = path.copy()
            new_path.append(cave)
            found_paths.append(new_path.copy())
        elif cave.islower() and cave in path:
            already_two = False
            for a_cave in path:
                if a_cave.islower() and path.count(a_cave) == 2:
                    already_two = True
                    break
            if not already_two:
                new_path = path.copy()
                new_path.append(cave)
                open_paths.append(new_path.copy())
        else:
            new_path = path.copy()
            new_path.append(cave)
            open_paths.append(new_path.copy())

print(len(found_paths))
