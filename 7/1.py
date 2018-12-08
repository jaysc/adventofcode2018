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

def Solution(order:list, nodesToProcess:list, node:Node):
    print(order);
    if node.name not in order:
        order.append(node.name);
    for nodeAfterName in node.after:
        nodeAfter = nodes[nodeAfterName];
        if node.name in nodeAfter.dependsOn:
            nodeAfter.dependsOn.remove(node.name);
        if len(nodeAfter.dependsOn) == 0 and nodeAfter not in nodesToProcess and nodeAfter.name not in order:
            nodesToProcess.append(nodeAfter)

    if len(nodesToProcess) != 0:
        SortNodes(initalNodes);
        nextNode = nodesToProcess.pop();
        Solution(order, nodesToProcess, nextNode)

    return order;

nextNode = initalNodes.pop();
print(''.join(Solution([],initalNodes,nextNode)));
