from re import search;

class Node(object):
    def __init__(self, name):
        self.name = name;
        self.dependsOn = set();
        self.after = set();

    def hasDepends(self):
        return len(self.dependsOn) != 0;

class Step(object):
    def __init__(self, step):
        parsedStep = search(r'Step (.) must be finished before step (.) can begin.', step.rstrip()); 
        
        self.before = parsedStep.group(1);
        self.after = parsedStep.group(2);

class Elf(object):
    def __init__(self):
        self.currentTime = 0;
        self.letter = None

    def ReachedLimit(self):
        return self.currentTime == (ord(self.letter) - 4);

nodes  = dict();

def SortNodes(nodes):
    nodes.sort(key = lambda x: x.name,reverse=True)

def GetNode(nodeName):
    if nodeName in nodes:
        node = nodes[nodeName];
    else:
        node = Node(nodeName);
        nodes[nodeName] = node;
    return node;

with open("input.txt", "r") as file:
    for line in file:
        step = Step(line);

        GetNode(step.before).after.add(step.after);
        GetNode(step.after).dependsOn.add(step.before);

initalNodes = []
for node in nodes.values():
    print('Node:{}; Pre:{}; After:{}'.format(node.name,node.dependsOn,node.after));
    if not node.hasDepends():
        initalNodes.append(node);

SortNodes(initalNodes);

def Solution(nodesToProcess:list):
    elves = [Elf() for i in range(5)];
    order = list();
    lettersInProgress = list();
    timer = -1;
    while len(nodesToProcess) != 0 or len(lettersInProgress) != 0:
        # print(order);

        for elf in elves:
            if elf.letter is not None:
                elf.currentTime += 1;
                if elf.ReachedLimit():
                    currentNode = nodes[elf.letter];
                    for afterNodeName in currentNode.after:
                        afterNode = nodes[afterNodeName];
                        if currentNode.name in afterNode.dependsOn:
                            afterNode.dependsOn.remove(currentNode.name);
                        if len(afterNode.dependsOn) == 0:
                            nodesToProcess.append(afterNode);

                    order.append(elf.letter);
                    lettersInProgress.remove(elf.letter);
                    elf.letter = None;
                    elf.currentTime = 0;
            if elf.letter is None and len(nodesToProcess) != 0:
                SortNodes(nodesToProcess);
                letterInProgress = nodesToProcess.pop();
                elf.letter = letterInProgress.name;
                lettersInProgress.append(letterInProgress.name);

        if len(nodesToProcess) == 0 and len(lettersInProgress) == 0:
            break;
        timer += 1;
    
    return timer;

print(Solution(initalNodes));