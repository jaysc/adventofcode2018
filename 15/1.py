grid = [];

units = set();
elves = set();
goblins = set();
walls = set();
class Unit(object):
    def __init__(self, x:int, y:int, race):
        self.x = x;
        self.y = y;
        self.race = race;
        self.hp = 200;
        self.attack = 3;

with open("test.txt", "r") as file:
    y = 0;
    for line in file.readlines():
        line = line.rstrip();
        x = 0;
        for c in line:
            if c == '#':
                walls.add(tuple([x,y]));
            elif c == 'E':
                elf = Unit(x,y,'E');
                elves.add(elf);
                units.add(elf);
            elif c == 'G':
                golbin = Unit(x,y,'G');
                goblins.add(golbin);
                units.add(golbin);
            x += 1;
        y += 1;

        noUnits = line.replace('G','.').replace('E','.');
        grid.append(list(noUnits));

def printGrid():
    printGrid = grid.copy();
    for line in printGrid:
        line = ['*' if c == '.' else c for c in line];
        for elf in elves:
            printGrid[elf.y][elf.x] = 'E';
        for golbin in goblins:
            printGrid[golbin.y][golbin.x] = 'G';
        print(' '.join(line))
    print(' ');

printGrid()

def DetermineOrder():
    order = list(units.copy());
    order.sort(key = lambda unit: (unit.y,unit.x));
    return order;

orders = DetermineOrder();
for unit in orders:
    print('Active: ', unit.x,unit.y)
    avaliablePositions = set();
    if unit.race == 'G':
        for elf in elves:
            if not set(tuple([elf.x+1,elf.y])).intersection(walls):
                avaliablePositions.add(tuple([elf.x+1,elf.y]));
            if not set(tuple([elf.x-1,elf.y])).intersection(walls):
                avaliablePositions.add(tuple([elf.x-1,elf.y]));
            if not set(tuple([elf.x,elf.y+1])).intersection(walls):
                avaliablePositions.add(tuple([elf.x,elf.y+1]));
            if not set(tuple([elf.x,elf.y-1])).intersection(walls):
                avaliablePositions.add(tuple([elf.x,elf.y-1]));

    else:
        for goblin in goblins:
            if not set(tuple([goblin.x+1,goblin.y])).intersection(walls):
                avaliablePositions.add(tuple([goblin.x+1,goblin.y]));
            if not set(tuple([goblin.x-1,goblin.y])).intersection(walls):
                avaliablePositions.add(tuple([goblin.x-1,goblin.y]));
            if not set(tuple([goblin.x,goblin.y+1])).intersection(walls):
                avaliablePositions.add(tuple([goblin.x,goblin.y+1]));
            if not set(tuple([goblin.x,goblin.y-1])).intersection(walls):
                avaliablePositions.add(tuple([goblin.x,goblin.y-1]));

    print(avaliablePositions)
