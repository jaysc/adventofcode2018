import datetime
from re import search
from enum import Enum

class RecordType(Enum):
    begin = 1
    fallAsleep = 2
    wakesUp = 3

class Record(object):
    def __init__(self, record):
        self.record = record.rstrip()

        parsedDate = search(r'\[(.+)\]', self.record)
        parsedAction = search(r'#(\d+)\s|(falls asleep)|(wakes up)', self.record)

        self.dateTime = datetime.datetime.strptime(parsedDate.group(1), '%Y-%m-%d %H:%M')
        
        if parsedAction.group(1) != None:
            self.guardID = parsedAction.group(1)
            self.recordType = RecordType.begin
        elif parsedAction.group(2) != None:
            self.recordType = RecordType.fallAsleep
        elif parsedAction.group(3) != None:
            self.recordType = RecordType.wakesUp

class Guard(object):
    def __init__(self, ID = -1):
        self.ID = ID

datesDay = {}
guards = {}
records = []
with open("input.txt", "r") as file:
    for line in file:
        records.append(Record(line))

    #We parsed the dateTime of the records and sort them
    records.sort(key = lambda x: x.dateTime)

    #Iterate through the sorted list and work out what each guard is doing
    for record in records:
        currentDate = None
        recordDate = record.dateTime.date()
        if record.dateTime.date() not in datesDay:
            datesDay[recordDate] = Guard()
            dayGuard = datesDay[recordDate]
        else:
            dayGuard = datesDay[recordDate]
        
        if record.recordType == RecordType.begin:
            #A case where a guard begins before the next day
            if dayGuard.ID == -1:
                dayGuard.ID = record.guardID
            else:
                datesDay[recordDate + datetime.timedelta(days=1)] = Guard(record.guardID)

#Stop pursuing this logic as it was going to answer the question easily
# However I do like how the classes and days are arranged into objects
# Seems like an nice organisation structure 