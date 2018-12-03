from collections import Counter

count2 = 0
count3 = 0
with open("input.txt", "r") as file:
    for line in file:
        #Counter from collections module can count the number of times a letter appears
        #We then store the values into a set(hashset)
        count = set(Counter(line).values())

        if 2 in count:
            count2 += 1
        if 3 in count:
            count3 += 1

    result = count2 * count3
    print(result)