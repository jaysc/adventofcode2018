
points = set()
with open("input.txt", "r") as file:
    for line in file:
        points.add(tuple([int(c) for c in line.rstrip().split(',')]))

minX = min(points, key=lambda x: x[0])[0]
minY = min(points, key=lambda x: x[1])[1]
maxX = max(points, key=lambda x: x[0])[0]
maxY = max(points, key=lambda x: x[1])[1]

def closestPoint(x ,y):
    distances = {}
    #works the distance from each point
    for point in points:
        distances[point] = abs(point[0] - x) + abs(point[1] - y)
    
    #Dictionary containing the point and its distance to x,y
    minPointDict = min(distances.items(), key = lambda x: x[1])
    minDistance = minPointDict[1] #Actual Distance

    #Check if point distance is shared by another
    count = 0
    for point, distance in distances.items():
        if (distance == minDistance):
            count += 1
            if count == 2:
                return None

    #if shared then no single closest point
    return minPointDict[0] if count == 1 else None

infinitePoints = set()
pointSize = {}
for x in range(maxX + 1):
    for y in range(maxY + 1):
        closest = closestPoint(x,y)

        if closest != None and closest not in infinitePoints:
            if x in (0, maxX) or y in (0, maxY):
                infinitePoints.add(closest)
                if (closest in pointSize):
                    del pointSize[closest]
                continue
            elif closest not in pointSize:
                pointSize[closest] = 1
            else:
                pointSize[closest] += 1

print(max(pointSize.items(), key = lambda x: x[1])[1])