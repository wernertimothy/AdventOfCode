import numpy as np
import matplotlib.pyplot as plt

with open('PuzzleInput_day13.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    points = []
    for k, line in enumerate(lines):
        if line == '' : break
        points.append([int(x) for x in line.split(',')])
    points = np.array(points)
    fold_data = lines[k+1:]
    folds = []
    for fold in fold_data:
        tmp = fold.split()[2]
        folds.append(tmp.split('='))

x_max = np.max(points[:,0])+1
y_max = np.max(points[:,1])+1

visible_dots = []

paper = np.zeros((y_max, x_max))
for point in points:
    x,y = point
    paper[y,x] = 1

visible_dots.append(np.count_nonzero(paper))

for fold in folds:
    ax = fold[0]
    at = int(fold[1])
    if ax == 'y':
        upper_paper = paper[:at,:]
        lower_paper = paper[at+1:,:]
        for k, line in enumerate(lower_paper):
            upper_paper[-1-k] += line
        paper = upper_paper
    if ax == 'x':
        left_paper = paper[:,:at]
        right_paper = paper[:,at+1:]
        for k, line in enumerate(left_paper.T):
            right_paper[:,-1-k] += line
        paper = right_paper
    visible_dots.append(np.count_nonzero(paper))

plt.spy(paper)
plt.show()