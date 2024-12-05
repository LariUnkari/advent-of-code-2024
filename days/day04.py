"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""


# Shared logic


def findHorizontal(data, width, height, patternForward, patternReverse, log_level):
    positions = [[0,0],[0,0],[0,0],[0,0]]
    count = 0
    row = 0
    
    while row < height:
        # No need to check if word doesn't fit on row
        length = width - 3
        
        col = 0
        while col < length:
            # Set col positions
            for i in range(len(positions)):
                positions[i][0] = col+i
            
            # Check if a normal pattern is found
            if verifyMatch(data, positions, patternForward):
                count += 1
                if log_level >= 2:
                    print(f"Found horizontal forward pattern at [{col}-{col+3}][{row}]")
                    
            # Check if a reverse pattern is found
            if verifyMatch(data, positions, patternReverse):
                count += 1
                if log_level >= 2:
                    print(f"Found horizontal reverse pattern at [{col}-{col+3}][{row}]")

            col += 1

        row += 1

        # Set row positions
        for i in range(len(positions)):
            positions[i][1] = row

    return count

def findVertical(data, width, height, patternForward, patternReverse, log_level):
    positions = [[0,0],[0,0],[0,0],[0,0]]
    count = 0
    col = 0
    
    while col < width:
        # No need to check if word doesn't fit on column
        length = height - 3
        
        row = 0
        while row < length:
            # Set row positions
            for i in range(len(positions)):
                positions[i][1] = row+i
            
            # Check if a normal pattern is found
            if verifyMatch(data, positions, patternForward):
                count += 1
                if log_level >= 2:
                    print(f"Found vertical   forward pattern at [{col}][{row}-{row+3}]")
                    
            # Check if a reverse pattern is found
            if verifyMatch(data, positions, patternReverse):
                count += 1
                if log_level >= 2:
                    print(f"Found vertical   reverse pattern at [{col}][{row}-{row+3}]")

            row += 1

        col += 1

        # Set col positions
        for i in range(len(positions)):
            positions[i][0] = col

    return count

def findDiagonal(data, angle, width, height, patternForward, patternReverse, log_level):
    positions = [[0,0],[0,0],[0,0],[0,0]]
    type = "descending" if angle == 1 else "ascending "
    count = 0

    row = 0 if angle == 1 else 3
    rowLength = height - 3 if angle == 1 else height
    
    while row < rowLength: # No need to check if word doesn't fit
        # Set row positions
        for i in range(len(positions)):
            positions[i][1] = row + (i if angle == 1 else -i)

        col = 0
        while col < width - 3: # No need to check if word doesn't fit
            # Set col positions
            for i in range(len(positions)):
                positions[i][0] = col+i
            
            # Check if a normal pattern is found
            if verifyMatch(data, positions, patternForward):
                count += 1
                if log_level >= 2:
                    print(f"Found diagonal   forward {type} pattern at {positions[0]}-{positions[3]}")
                    
            # Check if a reverse pattern is found
            if verifyMatch(data, positions, patternReverse):
                count += 1
                if log_level >= 2:
                    print(f"Found diagonal   reverse {type} pattern at {positions[0]}-{positions[3]}")

            col += 1

        row += 1

    return count

def verifyMatch(data, positions, pattern):
    for i, pos in enumerate(positions):
        if not(data[pos[1]][pos[0]] == pattern[i]):
            return False

    return True

    
# Main logic


def getResultPart1(data, width, height, log_level):
    patternForward = ['X', 'M', 'A', 'S']
    patternReverse = ['S', 'A', 'M', 'X']

    count = 0

    count += findHorizontal(data, width, height, patternForward, patternReverse, log_level)
    count += findVertical(data, width, height, patternForward, patternReverse, log_level)
    count += findDiagonal(data, 1, width, height, patternForward, patternReverse, log_level)
    count += findDiagonal(data, -1, width, height, patternForward, patternReverse, log_level)

    return (True, count)

def getResultPart2(data, width, height, log_level):
    mapped_data = []
    for n in range(height):
        mapped_data.append(['.'] * width)

    patternForward = ['M', 'A', 'S']
    patternReverse = ['S', 'A', 'M']
    
    positionsAscending = [[0,0],[0,0],[0,0]]
    positionsDescending = [[0,0],[0,0],[0,0]]

    matchAscending = False
    matchDescending = False
    count = 0

    row = 1
    rowLength = width - 1
    colLength = height - 1

    while row < rowLength:
        col = 1

        if log_level >= 1:
            print(f"Checking for cross patterns centered at row {row} between columns {col}-{colLength}")

        while col < colLength:

            if data[row][col] == 'A':
                if log_level >= 3:
                    print(f"Found a potential cross pattern at ({col},{row})")

                matchAscending = False
                matchDescending = False

                for i in range(3):
                    positionsAscending[i][0] = col + i - 1
                    positionsAscending[i][1] = row - i + 1
                    positionsDescending[i][0] = col + i - 1
                    positionsDescending[i][1] = row + i - 1

                if verifyMatch(data, positionsAscending, patternForward) or verifyMatch(data, positionsAscending, patternReverse):
                    matchAscending = True
                    if log_level >= 4:
                        print(f"Found ascending match: {positionsAscending}")

                if verifyMatch(data, positionsDescending, patternForward) or verifyMatch(data, positionsDescending, patternReverse):
                    matchDescending = True
                    if log_level >= 4:
                        print(f"Found descending match: {positionsDescending}")
                        
                if matchAscending and matchDescending:
                    count += 1
                    for posA in positionsAscending:
                        mapped_data[posA[1]][posA[0]] = data[posA[1]][posA[0]]
                    for posD in positionsDescending:
                        mapped_data[posD[1]][posD[0]] = data[posD[1]][posD[0]]

                    if log_level >= 2:
                        print(f"Found valid cross pattern at ({col},{row}), count now at {count}")
                elif log_level >= 2:
                    print(f"Cross pattern at ({col},{row}) was not valid")

            col += 1
        row += 1

    if log_level >= 1:
        for line in mapped_data:
            print(' '.join(line))

    return (True, count)

def play(input_data, day_part, log_level):

    #Initialize and read input

    parsed_data = []
    width = 0

    for index, line in enumerate(input_data):
        row = []
        stripped = line.strip()

        if width == 0:
            width = len(stripped)

        for char in stripped:
            row.append(char)

        parsed_data.append(row)

    height = len(parsed_data)

    print("Day 4 begins!")
    print(f"Data dimensions: {width}x{height}")

    if day_part == 0 or day_part == 1:
        #Result tuple format is (success <bool>, result <string>)
        resultPart1 = getResultPart1(parsed_data, width, height, log_level)

        if (resultPart1[0]):
            print(f"Answer to Part 1 is {resultPart1[1]}\n")
        else:
            print("Unable to find answer to Part 1\n")

    if day_part == 0 or day_part == 2:
        #Result tuple format is (success <bool>, result <string>)
        resultPart2 = getResultPart2(parsed_data, width, height, log_level)

        if (resultPart2[0]):
            print(f"Answer to Part 2 is {resultPart2[1]}\n")
        else:
            print("Unable to find answer to Part 2\n")