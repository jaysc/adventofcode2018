import datetime
import operator
from re import search
from enum import Enum

class RecordType(Enum):
    begin = 1
    fallAsleep = 2
    wakesUp = 3

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

class Guard(object):
    def __init__(self, ID):
        self.ID = int(ID)
        self.timeFellAsleep = -1
        self.timeAsleep = 0
        self.sleptAt = {}

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

#Everything prior is the same#

#Make a record of each guard most slept minute
sleepRecord = {}
for guard in guards.values():
    if len(guard.sleptAt) != 0:
        maxSleptAt = max(guard.sleptAt.items(), key=operator.itemgetter(1))
        key = '{}:{}'.format(guard.ID, maxSleptAt[0])
        sleepRecord[key] = maxSleptAt[1]

#Work out the minute and guard ID
guardSleptMostMinute = max(sleepRecord.items(), key=operator.itemgetter(1))
parsedMostMinute = search(r'(\d+):(\d+)', guardSleptMostMinute[0])

print(int(parsedMostMinute.group(1)) * int(parsedMostMinute.group(2)))