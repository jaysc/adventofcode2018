from re import search

class Claim(object):
    def __init__(self, claim):
        parseSearch = search(r'\#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', claim.rstrip())

        self.ID = parseSearch.group(1)
        self.x = parseSearch.group(2)
        self.y = parseSearch.group(3)
        self.width = parseSearch.group(4)
        self.height = parseSearch.group(5)
        

with open("input.txt", "r") as file:
    for line in file:
        claim = Claim(line)
        