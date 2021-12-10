# 2d arrays
import numpy as np
# visualization
import matplotlib.pyplot as plt

with open('PuzzleInput_day09.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    heightmap = [[int(height) for height in line] for line in lines]

length = len(heightmap)
width = len(heightmap[0])

low_points = []
risklevelsum = 0
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
            risklevelsum = risklevelsum + heightmap[i][j] + 1
            low_points.append((i,j))

print(risklevelsum)

# visualization
plt.imshow(heightmap,cmap='Greys')
for point in low_points:
    i, j = point
    plt.scatter(j,i, color='red', marker='.')
plt.show()
