#Very messy solution!

from collections import Counter
from difflib import ndiff

count2 = 0
count3 = 0
inputList = set()
with open("input.txt", "r") as file:
    for line in file:
        inputList.add(line.rstrip())
    #Sort the list! This means they are put next to the most common string
    inputList = sorted(inputList)

    for i, line in enumerate(inputList):
        #Compare current string to next
        if i + 1 == len(inputList):
            #Break if comparing second to last string
            break

        length = len(line)
        nextLine = inputList[i+1]
        
        #ndiff here to determine what changed between the two string.
        #returns 2 entries (-u,+g for example) meaning 1 difference between the two strings
        if len([changed for changed in ndiff(line, nextLine) if changed[0] != ' ']) == 2:
            
            #Probably not the best way to find the common letters
            #Can't use set union due to having to be in order.
            commonLetter = []
            for li, l in enumerate(line):
                nextLineLetter = nextLine[li]

                if l == nextLineLetter:
                    commonLetter.append(l)

            print(''.join(commonLetter))
            break