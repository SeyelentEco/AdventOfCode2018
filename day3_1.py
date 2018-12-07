import numpy as np
import re

def main():
    grid = np.zeros((1000,1000))
    countCollision = 0
    filename = 'day3_1_input.txt'
    userInput = open(filename, 'r')
    for line in userInput:
        #print(line)
        m = re.search("\\#(\d+) \\@ (\d+),(\d+): (\d+)x(\d+)", line)
        idx = int(m.group(1))
        startX = int(m.group(2))
        startY = int(m.group(3))
        sizeX = int(m.group(4))
        sizeY = int(m.group(5))

        #print ("startX", startX)
        #print ("startY", startY)
        #print ("sizeX", sizeX)
        #print ("sizeY", sizeY)

        for x in range(startX,startX+sizeX):
            for y in range(startY,startY+sizeY):
                if (grid[x][y] == 1):
                    countCollision += 1
                grid[x][y] += 1

    print (grid)
    print (countCollision)

main()
