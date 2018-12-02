sumValue = 0

with open("input.txt", "r") as file:
    for line in file:
        value = int(line)
        sumValue += value

print(sumValue)