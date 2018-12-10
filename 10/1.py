from re import findall;
from math import inf;
points = list();
with open("input.txt", "r") as file:
    for line in file:
        x, y, vx, vy =  map(int, findall(r'-?\d+', line.rstrip()));
        points.append([x,y,vx,vy]);

maxX = inf;
it = 0;
for i in range(100000):
    xValues = [x + (i * vx) for x, y, vx, vy in points];
    yValues = [y + (i * vy) for x, y, vx, vy in points];

    newMaxX = max(xValues)

    if newMaxX > maxX:
        it = i-1
        break;
    else:
        maxX = newMaxX;

if it != 0:
    xValues = [x + (it * vx) for x, y, vx, vy in points];
    yValues = [y + (it * vy) for x, y, vx, vy in points];
    minX = min(xValues);
    minY = min(yValues);
    maxY = max(yValues);

    #Rebase coordinates so they are from 0
    reMaxX = maxX - minX
    reMaxY = maxY - minY
    display = [['  ' for i in range(0, reMaxX+1)] for j in range(0, reMaxY+1)];

    for index in range(len(xValues)):
        display[yValues[index] - minY][xValues[index] - minX] = '#';

    for row in display:
        print(' '.join(row));

    print(it);