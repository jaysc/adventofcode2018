value = 170641;
initalScore = 37;
scores = [int(digit) for digit in str(initalScore)];

elf1 = 0;
elf2 = 1;
for i in range(value+11):
    total = scores[elf1] + scores[elf2];
    scores.extend(divmod(total, 10) if total >= 10 else [total]);
    
    elf1 = (elf1 + 1 + scores[elf1]) % len(scores);
    elf2 = (elf2 + 1 + scores[elf2]) % len(scores);

print(scores[value:value+10])