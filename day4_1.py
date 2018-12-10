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
    for guard in timeSleeping:
        if timeSleeping[guard] > maxTimeSleeping:
            maxTimeSleeping = timeSleeping[guard]
            maxGuard = guard

    minutesForGuard = hourDict[maxGuard]
    maxMin = 0
    maxValue = 0
    for min in range(0, 60):
        if (minutesForGuard[min] > maxValue):
            maxValue = minutesForGuard[min]
            maxMin = min
    print(maxGuard)
    print(maxMin)
    print(int(maxGuard) * maxMin)


main()
