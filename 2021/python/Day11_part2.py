import numpy as np

with open('PuzzleInput_day11.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    energy_levels = np.array([[int(char) for char in line] for line in lines])

steps = 0
while True:
    steps = steps + 1
    flashing = []
    energy_levels = energy_levels + 1
    for i in range(len(energy_levels)):
        for j in range(len(energy_levels[0])):
            if energy_levels[i,j] > 9:
                flashing.append((i,j))
    flashed = []
    while flashing:
        i,j = flashing.pop()
        flashed.append((i,j))
        for di in [-1,0,1]:
            i_new = i + di
            if i_new<0 or i_new==len(energy_levels):
                continue
            for dj in [-1,0,1]:
                j_new = j + dj
                if j_new<0 or j_new==len(energy_levels[0]):
                    continue
                if di==0 and dj==0:
                    continue
                energy_levels[i_new,j_new] = energy_levels[i_new,j_new] + 1
                if energy_levels[i_new,j_new] > 9 and (i_new,j_new) not in flashed and (i_new,j_new) not in flashing:
                    flashing.append((i_new,j_new))
    for octpous in flashed:
        energy_levels[octpous] = 0
    if len(flashed) == energy_levels.size:
       print(steps)
       break
    
