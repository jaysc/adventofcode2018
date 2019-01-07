trees = set();
lumberYards = set();
openLands = set();
def LookAround(x:int,y:int,type:str):
    checkAgainst = None;

    if type == '|':
        checkAgainst = trees.copy();
    elif type == '#':
        checkAgainst = lumberYards.copy();
    else:
        checkAgainst = openLands.copy();

    count = 0;
    for xv in range(x-1,x+2):
        if xv < 0:
            continue;
        for yv in range(y-1,y+2):
            if yv < 0 or (yv == y and xv == x):
                continue;
            if tuple([xv,yv]) in checkAgainst:
                count += 1;

    return count;


with open("input.txt", "r") as file:
    y = 0;
    for line in file.readlines():
        line = line.rstrip();

        x = 0;
        for c in line:
            if c == '#':
                lumberYards.add(tuple([x,y]));
            elif c == '|':
                trees.add(tuple([x,y]));
            else:
                openLands.add(tuple([x,y]));
            x += 1;
        y += 1; 

for minutes in range(1, 11):
    treesCache = trees.copy();
    landsCache = openLands.copy();
    lumbersCache = lumberYards.copy();
    for openLand in openLands:
        if LookAround(openLand[0],openLand[1], '|') >= 3:
            treesCache.add(tuple([openLand[0], openLand[1]]));
            landsCache.discard(tuple([openLand[0],openLand[1]]));
    for tree in trees:
        if LookAround(tree[0],tree[1], '#') >= 3:
            # print(LookAround(tree[0],tree[1], '#'));
            # print(tree[0], tree[1]);
            lumbersCache.add(tuple([tree[0], tree[1]]));
            treesCache.discard(tuple([tree[0],tree[1]]));
    for lumberYard in lumberYards:
        if (LookAround(lumberYard[0],lumberYard[1], '#') > 0
            and LookAround(lumberYard[0],lumberYard[1], '|') > 0):
                continue;
        else:
            # print(LookAround(lumberYard[0],lumberYard[1], '#'));
            # print(LookAround(lumberYard[0],lumberYard[1], '|'));
            # print(lumberYard[0], lumberYard[1]);
            landsCache.add(tuple([lumberYard[0], lumberYard[1]]));
            lumbersCache.discard(tuple([lumberYard[0],lumberYard[1]]));

    trees = treesCache.copy();
    openLands = landsCache.copy();
    lumberYards = lumbersCache.copy();
    print(len(trees) * len(lumberYards))
    

#Part 2.
#first cyclic at 407
#period of 28
#print((1000000000-407) % 28) = remainder
#print(407+remainder) = line number with our answer