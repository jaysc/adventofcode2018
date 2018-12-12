from re import search;

with open("test.txt", "r") as file:
    initalState = search(r'initial state: (.+)',file.readline().rstrip()).group(1);
    file.readline();
    plants = set();
    noPlants = set(); 
    for line in file:
        line = line.rstrip();
        if line[-1] == "#":
            plants.add(line[0:5]);
        else:
            noPlants.add(line[0:5]);


plantIndex = set(i for i, v in enumerate(initalState) if v == '#');

print(initalState);
initalState = list(initalState);

newPlantIndex = set();
for gen in range(1,21):
    for i in plantIndex:
        part = ''.join(['#' if i + j in plantIndex else '.' for j in [-2, -1, 0, 1, 2]])
        print(part);
        if part in plants:
            newPlantIndex.add(i);
    
    print(['#' if j in plantIndex else '.' for j in range(max(plantIndex))])
    plantIndex = newPlantIndex;
    newPlantIndex = set();