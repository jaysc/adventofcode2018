from re import search;

def addr(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] + tempReg[B];
    return tempReg;

def addi(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] + B;
    return tempReg;
    
def mulr(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] * tempReg[B];
    return tempReg;

def muli(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] * B;
    return tempReg;

def banr(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] & tempReg[B];
    return tempReg;

def bani(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] & B;
    return tempReg;

def borr(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] | tempReg[B];
    return tempReg;

def bori(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A] | B;
    return tempReg;

def setr(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = tempReg[A];
    return tempReg;

def seti(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = A;
    return tempReg;

def gtir(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = 1 if A > tempReg[B] else 0;
    return tempReg;

def gtri(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = 1 if tempReg[A] > B else 0;
    return tempReg;

def gtrr(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = 1 if tempReg[A] > tempReg[B] else 0;
    return tempReg;

def eqir(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = 1 if A == tempReg[B] else 0;
    return tempReg;

def eqri(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = 1 if tempReg[A] == B else 0;
    return tempReg;

def eqrr(reg:list,A:int,B:int,C:int):
    tempReg = reg.copy();
    tempReg[C] = 1 if tempReg[A] == tempReg[B] else 0;
    return tempReg;

def action(before:list,opcode:list,after:list, total:int):
    O = opcode[0]
    A = opcode[1];
    B = opcode[2];
    C = opcode[3];
    match = [0 for i in range(16)];
    match[0] = 1 if addr(before,A,B,C) == after and O == 10 else 0;
    match[1] = 1 if addi(before,A,B,C) == after and O == 15 else 0;
    match[2] = 1 if mulr(before,A,B,C) == after and O == 11 else 0;
    match[3] = 1 if muli(before,A,B,C) == after and O == 13 else 0;
    match[4] = 1 if banr(before,A,B,C) == after and O == 14 else 0;
    match[5] = 1 if bani(before,A,B,C) == after and O == 12 else 0;
    match[6] = 1 if borr(before,A,B,C) == after and O == 9 else 0;
    match[7] = 1 if bori(before,A,B,C) == after and O == 2 else 0;
    match[8] = 1 if setr(before,A,B,C) == after and O == 1 else 0;
    match[9] = 1 if seti(before,A,B,C) == after and O == 6 else 0;
    match[10] = 1 if gtir(before,A,B,C) == after and O == 0 else 0;
    match[11] = 1 if gtri(before,A,B,C) == after and O == 4 else 0;
    match[12] = 1 if gtrr(before,A,B,C) == after and O == 3 else 0;
    match[13] = 1 if eqir(before,A,B,C) == after and O == 5 else 0;
    match[14] = 1 if eqri(before,A,B,C) == after and O == 7 else 0;
    match[15] = 1 if eqrr(before,A,B,C) == after and O == 8 else 0;
    # if sum(match) == 1:
    #     print(before, opcode, after)
    #     print([i for i,v in enumerate(match) if v == 1])
    if sum(match) >= 3:
        total += 1;
    return total;
#opcode: 0 == gtir
#opcode: 1 == setr
#opcode: 2 == bori
#opcode: 3 == gtrr
#opcode: 4 == gtri
#opcode: 5 == eqir
#opcode: 6 == seti
#opcode: 7 == eqri
#opcode: 8 == eqrr
#opcode: 10 == addr
#opcode: 11 == mulr
#opcode: 12 == bani
#opcode: 13 == muli
#opcode: 14 == banr
#iocide: 15 == addi

total = 0;
with open("part1.txt", "r") as file:
    while True:
        line = file.readline();
        if line == '':
            break;
        if line != '\n':
            line = line.rstrip();
            before = list(map(int, search(r'\[(.+)\]', line).group(1).split(',')));
            line = file.readline().rstrip();
            opcode = list(map(int,line.split(' ')));
            line = file.readline().rstrip();
            after = list(map(int,search(r'\[(.+)\]', line).group(1).split(',')));
            total = action(before,opcode,after,total);

print(total);