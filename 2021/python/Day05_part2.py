# typehinting
from __future__ import annotations
from typing import List
# 2d array
import numpy as np

class Line:
    def __init__(self, line : List[List]) -> None:
        self._x1, self._y1 = line[0]
        self._x2, self._y2 = line[1]
        self._horizontal = (self._y1 == self._y2)
        self._vertical = (self._x1 == self._x2)

    @property
    def horizontal(self) -> bool:
        return self._horizontal

    @property
    def vertical(self) -> bool:
        return self._vertical

    @property
    def chords(self) -> List:
        return [self._x1, self._y1, self._x2, self._y2]

    def draw(self) -> List[List]:
        points = []
        # horizontal
        if self._vertical:
            if self._y1 > self._y2:
                for i in range(self._y1-self._y2+1):
                    points.append([self._x1, self._y2+i])
            elif self._y2 > self._y1:
                for i in range(self._y2-self._y1+1):
                    points.append([self._x1, self._y1+i])
            else:
                raise Exception('is this line a point?')
        # vertical
        elif self._horizontal:
            if self._x1 > self._x2:
                for i in range(self._x1-self._x2+1):
                    points.append([self._x2+i, self._y1])
            elif self._x2 > self._x1:
                for i in range(self._x2-self._x1+1):
                    points.append([self._x1+i, self._y1])
            else:
                raise Exception('is this line a point?')
        # diagonal
        else:
            if (self._x1<self._x2) and (self._y1>self._y2):
                Delta = self._x2-self._x1
                for i in range(Delta+1):
                    points.append([self._x1+i, self._y1-i])
            elif (self._x1<self._x2) and (self._y1<self._y2):
                Delta = self._x2-self._x1
                for i in range(Delta+1):
                    points.append([self._x1+i, self._y1+i])
            elif (self._x1>self._x2) and (self._y1<self._y2):
                Delta = self._x1-self._x2
                for i in range(Delta+1):
                    points.append([self._x1-i, self._y1+i])
            elif (self._x1>self._x2) and (self._y1>self._y2):
                Delta = self._x1-self._x2
                for i in range(Delta+1):
                    points.append([self._x1-i, self._y1-i])
            else:
                raise Exception('is this line a point?')
        return points

# read data
with open('PuzzleInput_day05.txt') as f:
    lines = f.readlines()
    lines = [line.strip().split(' -> ') for line in lines]
    lines = [[chords.split(',') for chords in line] for line in lines]
    lines = [[[int(pos) for pos in chords] for chords in line] for line in lines]
    grid_sizes = np.max(lines) + 1
    lines = [Line(line) for line in lines]

# draw
diagramm = np.zeros((grid_sizes,grid_sizes))
for line in lines:
    points = line.draw()
    for point in points:
        x,y = point
        diagramm[y,x] = diagramm[y,x]+1

# print(diagramm)
print((diagramm>=2).sum())