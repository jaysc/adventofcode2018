sumValue = 0
hashset = set()
with open("input.txt", "r") as file:
    #Assumes there will be a duplicate at one point
    while True:
        line = file.readline()
        if line == '':
            file.seek(0)
            line = file.readline()

        value = int(line)
        sumValue += value
        if sumValue in hashset:
            print(sumValue)
            break
        else:
            hashset.add(sumValue)