with open("input.txt", "r") as file:
    input = file.read().split(' ')

class Node(object):
    def __init__(self):
        self.childNodes = list();
        self.metaData = list();
        self.value = 0;

    def CalculateValue(self):
        if len(self.childNodes) == 0:
            self.value = sum(self.metaData);
        else:
            value = 0;
            for metadataValue in self.metaData:
                if metadataValue <= len(self.childNodes):
                    index = metadataValue - 1;
                    value += self.childNodes[index].value;
            self.value = value;

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
        node.childNodes.append(createNode(step)[0]);
    
    for i in range(metadataNum):
        step.increment();
        step.metaDataSum += step.number();
        node.metaData.append(step.number());

    #print('node has childNodes:{}; metaData:{}'.format(len(node.childNodes), node.metaData))
    #print(step.counter);
    node.CalculateValue();
    return node, step;

result, finalStep = createNode(Step(input));
print(result.value);