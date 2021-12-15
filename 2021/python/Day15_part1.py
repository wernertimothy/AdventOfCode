from collections import deque
import numpy as np
import matplotlib.pyplot as plt

risk_levels = []
with open('PuzzleInput_day15.txt') as f:
    data = f.readlines()
    for line in data:
        risk_levels.append([int(char) for char in line.strip()])
    risk_levels = np.array(risk_levels)

length, width = risk_levels.shape
start = (0,0)
goal = (length-1, width-1)

total_risk = np.inf*np.ones_like(risk_levels, dtype=int)
total_risk[start] = 0
chitons_to_check = deque([start])

k = 0
while chitons_to_check:
    k += 1
    i,j = chitons_to_check.popleft()
    for di in [-1,0,1]:
        inew = i + di
        if inew < 0 or inew == length:
            continue
        for dj in [-1,0,1]:
            jnew = j + dj
            if jnew < 0 or jnew == width:
                continue
            if abs(di) == abs(dj):
                continue
            new_risk = total_risk[(i,j)] + risk_levels[(inew,jnew)]
            if new_risk < total_risk[(inew,jnew)]:
                total_risk[(inew,jnew)] = new_risk
                if (inew,jnew) not in chitons_to_check:
                    chitons_to_check.append((inew,jnew))
    if k%500 == 0:
        plt.imshow(total_risk, cmap='Blues')
        plt.pause(0.001)
        plt.clf()

print(total_risk[goal])

chito = goal
reversed_path = [chito]
while chito != (start):
    previous_risk = total_risk[chito] - risk_levels[chito]
    i,j = chito
    for di in [-1,0,1]:
        inew = i + di
        if inew < 0 or inew == length:
            continue
        for dj in [-1,0,1]:
            jnew = j + dj
            if jnew < 0 or jnew == width:
                continue
            if abs(di) == abs(dj):
                continue
            if total_risk[(inew,jnew)] == previous_risk:
                chito = (inew,jnew)
                reversed_path.append(chito)
                break
        else:
            continue
        break

plt.imshow(total_risk, cmap='Blues')
for chito in reversed_path:
    i,j = chito
    plt.plot(j,i,'r.')
    plt.pause(0.001)
plt.show()
