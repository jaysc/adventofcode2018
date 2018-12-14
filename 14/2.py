value = [int(digit) for digit in str('170641')];
initalScore = 37;
scores = [int(digit) for digit in str(initalScore)];

elf1 = 0;
elf2 = 1;
while True:
    total = scores[elf1] + scores[elf2];
    scores.extend(divmod(total, 10) if total >= 10 else [total]);
    
    elf1 = (elf1 + 1 + scores[elf1]) % len(scores);
    elf2 = (elf2 + 1 + scores[elf2]) % len(scores);

    if scores[-len(value):] == value:
        print(scores[-len(value)-1:]);
        print(value);
        print('break!');
        break;

print(len(scores) - len(value))

#203184680