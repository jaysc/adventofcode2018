with open("input.txt", "r") as file:
    input = file.read().split(' ')

class Node(object):
    def __init__(self):
        self.childNodes = set();
        self.metaData = list();

class Step(object):
    def __init__(self, input):
        self.counter = 0;
        self.input = input;
        self.metaDataSum = 0;

    def increment(self):
        self.counter += 1;

    def number(self):
        return int(self.input[self.counter]);

def createNode(step:Step):
    node = Node();
    #print('counter:{}'.format(step.counter))
    childNodesNum = step.number();
    #print('childNodesNum:{}'.format(childNodesNum))
    step.increment();
    metadataNum = step.number();
    #print('metadataNum:{}'.format(metadataNum))

    for i in range(childNodesNum):
        step.increment();
        node.childNodes.add(createNode(step));
    
    for i in range(metadataNum):
        step.increment();
        step.metaDataSum += step.number();
        node.metaData.append(step.number());

    #print('node has childNodes:{}; metaData:{}'.format(len(node.childNodes), node.metaData))
    #print(step.counter);
    return node, step;

result, finalStep = createNode(Step(input));
print(finalStep.metaDataSum);