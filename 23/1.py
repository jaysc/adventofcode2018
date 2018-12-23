from re import search;
import z3;

def IsWithinRange(o:tuple,c:tuple, r:int):
    return abs(o[0]-c[0]) + abs(o[1]-c[1]) + abs(o[2]-c[2]) <= r;

coords = dict();
with open("input.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip();
        
        parsedLine = search(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', line);
        x,y,z,r = map(int,parsedLine.groups());

        coords[tuple([x,y,z])] = r;

orderedCoords = sorted(coords.items(), key = lambda x: x[1], reverse=True);
largestCoords = max(coords.items(), key = lambda x: x[1]);

totalInRange = 0;
for bot in range(1,len(orderedCoords)):
    if IsWithinRange(largestCoords[0], orderedCoords[bot][0], largestCoords[1]):
        totalInRange += 1;

print(totalInRange + 1)