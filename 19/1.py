from re import search;
from re import findall;

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

def Doaction(before:list,opcode:list):
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

def resolveAction(action:str):
    result = None;
    if action == 'gtir':
        result = 0;
    elif action == 'setr':
        result = 1;
    elif action == 'bori':
        result = 2;
    elif action == 'gtrr':
        result = 3;
    elif action == 'gtri':
        result = 4;
    elif action == 'eqir':
        result = 5;
    elif action == 'seti':
        result = 6;
    elif action == 'eqri':
        result = 7;
    elif action == 'eqrr':
        result = 8;
    elif action == 'borr':
        result = 9;
    elif action == 'addr':
        result = 10;
    elif action == 'mulr':
        result = 11;
    elif action == 'bani':
        result = 12;
    elif action == 'muli':
        result = 13;
    elif action == 'banr':
        result = 14;
    elif action == 'addi':
        result = 15;

    return result;

class instruct(object):
    def __init__(self, action:int, A:int, B:int, C:int):
        self.action = action;
        self.A = A;
        self.B = B;
        self.C = C;


bound = None;
registers = [1,0,0,0,0,0];
instructions = [];
with open("input.txt", "r") as file:
    line = file.readline().rstrip();
    bound = int(search(r'#ip (\d+)', line).group(1));

    for line in file.readlines():
        line = line.rstrip();
        parsedLine = search(r'(\w+) (\d+) (\d+) (\d+)', line);
        action = resolveAction(parsedLine.group(1));
        A = parsedLine.group(2);
        B = parsedLine.group(3);
        C = parsedLine.group(4);
        action, A,B,C = map(int, [action, A,B,C]);
        instructions.append(instruct(action, A, B, C));
a = 0
finish = False;
ip = 0;
while ip < len(instructions) and a < 1000:
    a += 1;
    if (ip == 9):
        registers[1] = registers[5] + 1
    if ip == 14:
        registers[3] = registers[5] + 1
    print(ip)
    #print(registers);
    i = instructions[ip];
    #print([i.action, i.A,i.B,i.C])
    registers[bound] = ip;
    registers = Doaction(registers,[i.action, i.A, i.B, i.C]);
    ip = registers[bound];
    ip += 1;
    if (ip == 14):
        #print(a)
        print([i.action, i.A,i.B,i.C])
        print(registers);

print(registers);
