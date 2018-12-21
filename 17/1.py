from re import search;

sourcePoints = [[500,0]];
waters = set(tuple([500,0]));
clay = set();
with open("test.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip();
        parsedx = search(r'x=([\d\.]+)', line);
        parsedy = search(r'y=([\d\.]+)', line);
        x = list(map(int,parsedx.group(1).split('..')));
        if len(x) == 2:
            x = range(x[0],x[1]+1)
        y = list(map(int,parsedy.group(1).split('..')));
        if len(y) == 2:
            y = range(y[0],y[1]+1)
        for xvalues in x:
            for yvalues in y:
                clay.add(tuple([xvalues, yvalues]));

for i in range(50):
    sourcePoints = sorted(sourcePoints, key = lambda sourcePoint: (sourcePoint[1], sourcePoint[0]));

    for sourcePoint in sourcePoints:
        hit = False;
        while not hit:
            if tuple([sourcePoint[0], sourcePoint[1] + 1]) not in clay:
                print("hit");
                sourcePoint[1] += 1;
            else:
                hit = True;


        if (sourcePoint[0]-1, sourcePoint[1]) not in clay:
            print("sideLeft");
            sideLeft = False;
            currentLeftWater = sourcePoint.copy();
            while not sideLeft:
                if (tuple([currentLeftWater[0],currentLeftWater[1] + 1]) in clay
                    and tuple([currentLeftWater[0]-1,currentLeftWater[1]]) not in clay):
                    currentLeftWater = [currentLeftWater[0]-1, currentLeftWater[1]];
                else:
                    sideLeft = True;
        print(tuple([sourcePoint[0], sourcePoint[1]]))

            # sideRight = False;
            # while not sideRight:
            #     if ((sourcePoint[0]+1, sourcePoint[1]) not in clay
            #         and (sourcePoint[0], sourcePoint[1] + 1) not in clay):
            #         sourcePoint[0] += 1;
            #     else:
            #         sideRight = True;