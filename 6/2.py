limit = 10000

points = set()
with open("input.txt", "r") as file:
    for line in file:
        points.add(tuple([int(c) for c in line.rstrip().split(',')]))

minX = min(points, key=lambda x: x[0])[0]
minY = min(points, key=lambda x: x[1])[1]
maxX = max(points, key=lambda x: x[0])[0]
maxY = max(points, key=lambda x: x[1])[1]

count = 0
for x in range(maxX + 1):
    for y in range(maxY + 1):

        distance = 0
        for point in points:
            distance += abs(point[0] - x) + abs(point[1] - y)
            if distance >= limit:
                break
        if distance >= limit:
            continue
        else:
            count += 1

print(count)