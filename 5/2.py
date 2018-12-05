import operator

data = ""
with open("input.txt", "r") as file:
    data = file.read().rstrip()

data = list(data)
letters = set(l.lower() for l in data)

def processUnitLength(ignore = None):
    stash = []
    for unit in data:
        if (ignore is not None 
            and (ignore == unit or ignore.capitalize() == unit)):
            continue

        if len(stash) == 0:
            stash.append(unit)
        else:
            stashLetter = stash[-1]
            if (abs(ord(stashLetter) - ord(unit)) == 32
                and (
                    (unit.isupper() and stashLetter.capitalize() == unit)
                    or (unit.islower() and unit.capitalize() == stashLetter)
                    )
                ):
                stash.pop()
            else:
                stash.append(unit)
    return len(''.join(stash))

#Here we iterate through all the letters we're going to ignore.
stashLength = {}
for letter in letters:
    stashLength[letter] = processUnitLength(letter)

print(min(stashLength.items(), key=operator.itemgetter(1)))