def main():
    totalNum = 0
    totalValues = {}
    filename = 'day1_1_input.txt'
    found = False
    while not found:
        userInput = open(filename, 'r')
        print ("Starting from the top")
        for i in userInput:
            print (i)
            if i[0] == '-':
                totalNum -= int(i[1:])
            else:
                totalNum += int(i[1:])
            print (totalNum)

            if totalNum in totalValues:
                found = True
                break
            else:
                totalValues[totalNum] = 1
        userInput.close()
    print(totalNum)

main()
