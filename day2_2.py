def main():
    lines = []
    filename = 'day2_1_input.txt'
    userInput = open(filename, 'r')
    print ("Starting from the top")
    for line in userInput:
        lines.append(line)
    for idx, cur in enumerate(lines):
        print(idx)
        for other in lines[idx:]:
            errorCount = 0
            lastErrorIndex = -1
            for x in range(0, len(cur)):
                if cur[x] != other[x]:
                    errorCount += 1
                    if (errorCount > 1):
                        break
                    else:
                        lastErrorIndex = x
            if errorCount == 1:
                print(cur)
                print(other)
                print(cur[0:lastErrorIndex-1] + cur[lastErrorIndex:])





main()
