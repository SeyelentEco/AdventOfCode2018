import re

def main():
    filename = 'day4_1_input.txt'
    userInput = open(filename, 'r')
    lines = []
    for line in userInput:
        lines.append(line)
    lines.sort()

    timeSleeping = {}
    hourDict = {}

    currentGuard = 0
    minuteAsleep = 0
    for record in lines:
        m = re.search("\\[(\d+)\\-(\d+)\\-(\d+) (\d+)\\:(\d+)\\] (.*)", record)
        #print(record)
        year = int(m.group(1))
        month = int(m.group(2))
        day = int(m.group(3))
        hour = int(m.group(4))
        minute = int(m.group(5))
        action = str(m.group(6))

        guardStart = re.search("Guard \\#(\d+) begins shift", action)
        if guardStart:
            currentGuard = guardStart.group(1)
            if currentGuard not in timeSleeping:
                timeSleeping[currentGuard] = 0
                hourDict[currentGuard] = {}
                for min in range(0, 60):
                    hourDict[currentGuard][min] = 0
        elif action == "falls asleep":
            minuteAsleep = minute
        else:
            timeSleeping[currentGuard] += (minute - minuteAsleep)
            for min in range(minuteAsleep, minute):
                hourDict[currentGuard][min] += 1

    #print (timeSleeping)
    #print (hourDict)

    maxGuard = 0
    maxTimeSleeping = 0
    maxMinForGuard = {}
    for guard in hourDict:
        maxMin = 0
        maxValue = 0
        for min in range(0, 60):
            if (hourDict[guard][min] > maxValue):
                maxValue = hourDict[guard][min]
                maxMin = min
        maxMinForGuard[guard] = {'val': maxValue, 'min': maxMin}

    #print(maxMinForGuard)
    maxGuard = 0
    maxVal = 0
    for guard in maxMinForGuard:
        if maxMinForGuard[guard]['val'] > maxVal:
            maxVal = maxMinForGuard[guard]['val']
            maxGuard = guard

    print(maxGuard)
    print(maxMinForGuard[maxGuard]['min'])
    print(int(maxGuard) * maxMinForGuard[maxGuard]['min'])


main()
