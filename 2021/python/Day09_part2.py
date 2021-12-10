# 2d arrays
import numpy as np
# visualization
import matplotlib.pyplot as plt
# deque
from collections import deque

with open('PuzzleInput_day09.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    heightmap = [[int(height) for height in line] for line in lines]

length = len(heightmap)
width = len(heightmap[0])

low_points = []
for i in range(length):
    for j in range(width):
        adjacent = []
        for di in [-1,0,1]:
            i_new = i + di
            if i_new < 0 or i_new == length:
                continue
            for dj in [-1,0,1]:
                j_new = j + dj
                if j_new < 0 or j_new == width:
                    continue
                if abs(di)==abs(dj):
                    continue
                adjacent.append(heightmap[i_new][j_new])
        if (np.array([heightmap[i][j] - height for height in adjacent])<0).all():
            low_points.append((i,j))

basins = []
for low_point in low_points:
    basin = []
    need_to_visit = deque([low_point])
    while need_to_visit:
        i,j = need_to_visit.pop()
        basin.append((i,j))
        for di in [-1,0,1]:
            i_new = i + di
            if i_new < 0 or i_new == length:
                continue
            for dj in [-1,0,1]:
                j_new = j + dj
                if j_new < 0 or j_new == width:
                    continue
                if abs(di)==abs(dj):
                    continue
                if heightmap[i_new][j_new] == 9:
                    continue
                else:
                    if (i_new,j_new) not in basin and (i_new,j_new) not in need_to_visit:
                        need_to_visit.append((i_new,j_new))
    basins.append(basin)

basin_sizes = [len(basin) for basin in basins]
print(np.prod(sorted(basin_sizes)[-3:]))