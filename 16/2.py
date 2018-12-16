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

def action(before:list,opcode:list):
    O = opcode[0]
    A = opcode[1];
    B = opcode[2];
    C = opcode[3];
    newReg = before.copy();
    if O == 0:
        newReg = gtir(before,A,B,C);
    elif O == 1:
        newReg = setr(before,A,B,C);
    elif O == 2:
        newReg = bori(before,A,B,C);
    elif O == 3:
        newReg = gtrr(before,A,B,C);
    elif O == 4:
        newReg = gtri(before,A,B,C);
    elif O == 5:
        newReg = eqir(before,A,B,C);
    elif O == 6:
        newReg = seti(before,A,B,C);
    elif O == 7:
        newReg = eqri(before,A,B,C);
    elif O == 8:
        newReg = eqrr(before,A,B,C);
    elif O == 9:
        newReg = borr(before,A,B,C);
    elif O == 10:
        newReg = addr(before,A,B,C);
    elif O == 11:
        newReg = mulr(before,A,B,C);
    elif O == 12:
        newReg = bani(before,A,B,C);
    elif O == 13:
        newReg = muli(before,A,B,C);
    elif O == 14:
        newReg = banr(before,A,B,C);
    elif O == 15:
        newReg = addi(before,A,B,C);

    # if sum(match) == 1:
    #     print(before, opcode, after)
    #     print([i for i,v in enumerate(match) if v == 1])
    return newReg;
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

reg = [0,0,0,0];
with open("part2.txt", "r") as file:
    for line in file.readlines():
        line = line.rstrip();
        print(line);
        opCode = list(map(int,line.split(' ')))

        reg = action(reg,opCode);

print(reg)