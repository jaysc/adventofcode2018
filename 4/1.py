import datetime
import operator
from re import search
from enum import Enum

#Enum
class RecordType(Enum):
    begin = 1
    fallAsleep = 2
    wakesUp = 3

#Record object for each line
class Record(object):
    def __init__(self, record):
        self.raw = record.rstrip()

        parsedDate = search(r'\[(.+)\]', self.raw)
        parsedAction = search(r'#(\d+)\s|(falls asleep)|(wakes up)', self.raw)

        self.dateTime = datetime.datetime.strptime(parsedDate.group(1), '%Y-%m-%d %H:%M')

        if parsedAction.group(1) != None:
            self.guardID = parsedAction.group(1)
            self.recordType = RecordType.begin
        elif parsedAction.group(2) != None:
            self.recordType = RecordType.fallAsleep
        elif parsedAction.group(3) != None:
            self.recordType = RecordType.wakesUp

#Guard object
class Guard(object):
    def __init__(self, ID):
        self.ID = int(ID)
        self.timeFellAsleep = -1
        self.timeAsleep = 0
        self.sleptAt = {} #Used to work out at what time slept the most

guards = {}
records = []
with open("input.txt", "r") as file:
    for line in file:
        records.append(Record(line))

    #We parsed the dateTime of the records and sort them
    records.sort(key = lambda x: x.dateTime)

#Iterate through the sorted list and work out what each guard is doing
currentGuard = None
for r in records:
    if r.recordType == RecordType.begin:
        if r.guardID not in guards:
            guards[r.guardID] = Guard(r.guardID)

        currentGuard = guards[r.guardID]
        next
    
    #We can assume currentGaurd is still active
    elif r.recordType == RecordType.fallAsleep:
        currentGuard.timeFellAsleep = r.dateTime
        next

    #Guard woke up! calculate time asleep
    elif r.recordType == RecordType.wakesUp:
        tDelta = r.dateTime - currentGuard.timeFellAsleep
        minutesAsleep = int(tDelta.total_seconds()/60)
        currentGuard.timeAsleep += minutesAsleep

        for minute in range(currentGuard.timeFellAsleep.minute, r.dateTime.minute):
            if minute not in currentGuard.sleptAt:
                currentGuard.sleptAt[minute] = 1
            else:
                currentGuard.sleptAt[minute] += 1
        next

#Work out the guard with the highest time asleep
resultGaurd = None
for guard in guards.values():
    if resultGaurd is None:
        resultGaurd = guard
    else:
        if guard.timeAsleep > resultGaurd.timeAsleep:
            resultGaurd = guard

#Find that guards most slept minute
guardMaxMinute = max(resultGaurd.sleptAt.items(), key=operator.itemgetter(1))[0]
print(resultGaurd.ID * guardMaxMinute)