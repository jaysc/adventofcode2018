from re import search
from collections import Counter

#Class to represent Claim
#Works out the xStart index and xEnd index
class Claim(object):
    def __init__(self, claim):
        #Regex to split string into components
        parseSearch = search(r'\#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', claim.rstrip())

        self.ID = int(parseSearch.group(1))
        self.x = int(parseSearch.group(2))
        self.y = int(parseSearch.group(3))
        self.width = int(parseSearch.group(4))
        self.height = int(parseSearch.group(5))

        self.xEnd = self.x + self.width
        self.yEnd = self.y + self.height
        
#Initialise 2d array
fabric = [[0 for i in range(1000)] for i in range(1000)]

with open("input.txt", "r") as file:
    for line in file:
        claim = Claim(line)

        #For each coordinate, we increment the overlap counter
        for x in range(claim.x,claim.xEnd):
            for y in range(claim.y, claim.yEnd):
                fabric[x][y] += 1

    #Use of counter to work out how many times it overlaps on each coordinate
    #Use of counter arithmatic to work out global counter for incrementing each row
    globalCounter = Counter()
    for row in fabric:
        globalCounter += Counter(row)
    
    #Final prints out sum of all overlaps that are greater than 1 (2 onwards)
    print(sum([v for i, v in dict(globalCounter).items() if i >= 2]))