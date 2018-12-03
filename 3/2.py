from re import search
from collections import Counter

class Claim(object):
    def __init__(self, claim):
        parseSearch = search(r'\#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)', claim.rstrip())

        self.ID = int(parseSearch.group(1))
        self.x = int(parseSearch.group(2))
        self.y = int(parseSearch.group(3))
        self.width = int(parseSearch.group(4))
        self.height = int(parseSearch.group(5))

        self.xEnd = self.x + self.width
        self.yEnd = self.y + self.height
        
#2d Array will now contain a list of claimIDs
fabric = [[[] for i in range(1000)] for i in range(1000)]
with open("input.txt", "r") as file:
    #List of all the claimIDs
    claims = []
    for line in file:
        claim = Claim(line)
        claims.append(claim.ID)

        for x in range(claim.x,claim.xEnd):
            for y in range(claim.y, claim.yEnd):
                squareClaims = (fabric[x][y])
                #We append the claimID to the list stored at the coordinate
                squareClaims.append(claim.ID)

                #If there are 2 claimIDs on the square, that means it's an overlap
                if len(squareClaims) > 1:
                    for claimID in squareClaims:
                        #We remove the claimID from claim for all the claimIDs on the list
                        if claimID in claims:
                            claims.remove(claimID)

    #Expect to see 1 claimID left (as per question)
    print(claims)

#For both questions, I found the implamentation to be messy and unoptimised, however it does the job. I have ideas on other
#ways to make it better like instead of storing an 2d array full, mark down start and end coordinates then check when a
#new claim enters the range - something like that or similar might work but not sure.