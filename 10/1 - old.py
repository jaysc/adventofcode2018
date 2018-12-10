from re import search;
from re import search;
from math import inf;
from copy import deepcopy;

class Point(object):
    def __init__(self, line:str):
        parse = search(r'position=<(.+), (.+)> velocity=<(.+),(.+)>', line.rstrip());

        self.x = int(parse.group(1));
        self.y = int(parse.group(2));
        self.vx = int(parse.group(3));
        self.vy = int(parse.group(4));

    def move(self):
        self.x += self.vx;
        self.y += self.vy;

points = list();
with open("input.txt", "r") as file:
    for line in file:
        points.append(Point(line));

minX = -inf;
minY = -inf;
maxX = inf;
maxY = inf;
final = list();
for i in range(10):
    for point in points:
        point.move()

    newMaxX = max([point.x for point in points if point.x >= 0]);
    newMaxY = max([point.y for point in points if point.y >= 0]);
    
    minX = max(min([point.x for point in points if point.x <= 0]), minX);
    minY = max(min([point.y for point in points if point.y <= 0]), minY);

    if newMaxX > maxX and newMaxY > maxY:
        print(i)
        break;
    else:
        final = deepcopy(points);
        maxX = newMaxX;
        maxY = newMaxY;

print('done')
display = [['  ' for i in range(minX, maxX+1)] for j in range(minY, maxY+1)];
for point in final:
    display[point.y][point.x] = '#';

for row in display:
    print(' '.join(row));