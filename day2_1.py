def main():
    linesWithTwo = 0
    linesWithThree = 0

    filename = 'day2_1_input.txt'
    userInput = open(filename, 'r')
    print ("Starting from the top")
    for line in userInput:
        totalValues = {}
        for char in line:
            if char in totalValues:
                totalValues[char] += 1
            else:
                totalValues[char] = 1
        print (line)
        prevTwo = linesWithTwo
        prevThree = linesWithThree
        for key in totalValues:
            if totalValues[key] == 2:
                linesWithTwo = prevTwo + 1
            if totalValues[key] == 3:
                linesWithThree = prevThree + 1

        print (str(linesWithTwo) + " " + str(linesWithThree))
    print (linesWithTwo * linesWithThree)

main()
