import networkx as nx;

#test
depth = 510;
target = tuple([10,10])

#input
depth = 3879;
target = tuple([8,713])

globalErosionLevel = dict();
globalType = dict();
def GetErosionLevel(x:int,y:int):
    gi = None;

    if (x == 0 and y == 0) or tuple([x,y]) == target:
        gi = 0;
    elif x == 0:
        gi = y * 48271;
    elif y == 0:
        gi = x * 16807;
    else:
        gi = globalErosionLevel[tuple([x-1,y])] * globalErosionLevel[tuple([x,y-1])];
    erosionLevel = (gi + depth) % 20183;

    globalErosionLevel[tuple([x,y])] = erosionLevel;
    return erosionLevel;

def GetType(x:int,y:int):
    localType = GetErosionLevel(x,y) % 3;
    globalType[tuple([x,y])] = localType;
    return localType;

maxX = target[0] + 100;
maxY = target[1] + 100;
for x in range(maxX + 1):
    for y in range (maxY + 1):
        GetType(x,y);

globalGridType = [[None for y in range(maxY + 1)] for x in range(maxX + 1)];
for cord, t in globalType.items():
    # c = "";
    # if cord == tuple([0,0]):
    #     c = "M";
    # elif cord == target:
    #     c = "T";
    # elif t == 0:
    #     c = '.';
    # elif t == 1:
    #     c = '=';
    # elif t == 2:
    #     c = '|';
    globalGridType[cord[0]][cord[1]] = t;

r,w,nar = 0,1,2;
t,g,n = 0,1,2;
items = {0:(t,g),1:(g,n),2:(t,n)};
#Part 2 was difficult. Had to consult solutions.
graph = nx.Graph();
for y in range(maxY + 1):
    for x in range (maxX + 1):
        item = items[globalGridType[x][y]];
        graph.add_edge((x, y, item[0]), (x, y, item[1]), weight=7)
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            newx, newy = x + dx, y + dy;
            if 0 <= newx <= maxX and 0 <= newy <= maxY:
                newItem = items[globalGridType[newx][newy]]
                for itemPart in set(item).intersection(set(newItem)):
                    graph.add_edge((x, y, itemPart), (newx, newy, itemPart), weight=1)

print(nx.dijkstra_path_length(graph, (0, 0, t), (target[0], target[1], t)))


# # for line in globalGridType:
# #     print(' '.join(line));

# riskTotal = 0;
# for cord, t in globalType.items():
#     if cord[0] <= target[0] and cord[1] <= target[1]:
#         riskTotal += t;

# print(riskTotal)
