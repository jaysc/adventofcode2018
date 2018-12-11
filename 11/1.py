
import numpy;
s = 5177

def powerLevel(x, y):
    v = (((x+10) * y) + s) * (x + 10);
    return ((v // 100) % 10) - 5;

def result(x,y):
    print(grid[x-1][y-1]);

grid = numpy.fromfunction(powerLevel, (300, 300));
l = grid.shape[1]+1;

locationList = [];
for w in range(3,300):
    summing = sum([grid[x:(l+x-w),y:(l+y-w)] for x in range(w) for y in range(w)])
    maxSum = summing.max();
    if maxSum < 0:
        break;
    location = numpy.where(summing == maxSum);
    locationList.append([location,maxSum, w]);

largestLocation = max(locationList, key = lambda location: location[1])
print(largestLocation[0][0],largestLocation[0][1], largestLocation[2])