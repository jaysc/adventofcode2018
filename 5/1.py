data = ""
with open("input.txt", "r") as file:
    data = file.read().rstrip()

data = list(data)

#The idea is similar to other puzzles.
#Use of a stash or stack as we go along to handle the logic
stash = []
for unit in data:
    if len(stash) == 0:
        stash.append(unit)
    else:
        stashLetter = stash[-1]
        #First does an easy check of whether it is valid or not
        #32 is the difference between ascii values of lower and upper case
        #We then directly check whether there are actually same letters or not
        #since the difference be achieved indirectly
        if (abs(ord(stashLetter) - ord(unit)) == 32
            and (
                (unit.isupper() and stashLetter.capitalize() == unit)
                or (unit.islower() and unit.capitalize() == stashLetter)
                )
            ):
            stash.pop()
        else:
            stash.append(unit)
    
print(len(''.join(stash)))
