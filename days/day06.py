"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""


TILE_OBSTACLE = '#'
TILE_FLOOR = '.'
DIR_NORTH = (0,-1)
DIR_EAST = (1,0)
DIR_SOUTH = (0,1)
DIR_WEST = (-1,0)
DIRECTIONS = [DIR_NORTH, DIR_EAST, DIR_SOUTH, DIR_WEST]


def isWithinBounds(x, y, width, height):
    return x >= 0 and x < width and y >= 0 and y < height

def walkUntilObstacle(mapData, x, y, d, width, height, path, visitedMap, log_level):
    tile = TILE_FLOOR
    i = 0
    nx = 0
    ny = 0
    loops = 0

    while True:
        nx = x + DIRECTIONS[d][0]
        ny = y + DIRECTIONS[d][1]

        if nx >= 0 and nx < width and ny >= 0 and ny < height:
            tile = mapData[ny][nx]

            if tile == TILE_OBSTACLE:
                return (True, x, y)
            else:
                x = nx
                y = ny
                i = y * width + x
                visitedMap[i] = True
                path.append((i, x, y, d))
                
                if log_level >= 2:
                    print(f"Now at position ({x},{y}), count: {visitedMap.count(True)}")
        else:
            if log_level >= 1:
                print(f"Stepped out of bounds at position ({nx},{ny})")

            return (True, nx, ny)

        loops += 1
        if loops > 1000:
            print("Emergency brake! Too many steps to find obstacle!")
            break

    return (False, nx, ny)

def walkUntilOutOfBounds(mapData, width, height, guardPosition, guardDirection, path, visitedMap, log_level):
    x = guardPosition[0]
    y = guardPosition[1]
    d = guardDirection

    walk = None
    loops = 0
    while True:
        walk = walkUntilObstacle(mapData, x, y, d, width, height, path, visitedMap, log_level)

        if walk[0]:
            x = walk[1]
            y = walk[2]

            if isWithinBounds(x, y, width, height):
                d = d + 1 if d < 3 else 0

                if log_level >= 1:
                    print(f"Obstacle at position ({x},{y}), turning right to direction {d}")
            else:
                break

        loops += 1
        if loops > 1000:
            print("Emergency brake! Too many steps to find out of bounds!")
            break

def getResultPart1(visitedMap):
    return (True, visitedMap.count(True))


def getResultPart2(mapData, width, height, startPos, startDir, originalPath, visitedMap, log_level):
    foundLoops = 0
    length = len(originalPath)

    print(f"Checking loops from {length} path positions")

    position = None
    walk = None
    si = 0
    sx = 0
    sy = 0
    sd = 0
    i = 0
    x = 0
    y = 0
    d = 0

    for p in range(length-1):
        # Start position and direction
        position = originalPath[p]
        si = position[0]
        sx = position[1]
        sy = position[2]
        sd = position[3]

        # Obstacle position
        ox = sx + DIRECTIONS[sd][0]
        oy = sy + DIRECTIONS[sd][1]
        oi = oy * width + ox

        # No need to test for loop if obstacle position already is an obstacle
        if mapData[oy][ox] == TILE_OBSTACLE:
            continue

        # Current position and direction
        x = sx
        y = sy
        i = si
        d = sd
        
        # Open tile found, check if making it an obstacle creates a loop
        mapData[oy][ox] = TILE_OBSTACLE
        path = []

        iterations = 0
        while True:
            d = d + 1 if d < 3 else 0
            walk = walkUntilObstacle(mapData, x, y, d, width, height, path, visitedMap, log_level - 1)

            if walk[0]:
                x = walk[1]
                y = walk[2]

                if isWithinBounds(x, y, width, height):
                    if x == sx and y == sy and d == sd:
                        foundLoops += 1

                        if log_level >= 1:
                            print(f"Loop found from path position {p} at ({sx},{sy}) in direction {sd}, obstacle at ({ox},{oy}), count now {foundLoops}!")

                        break
                else:
                    if log_level >= 2:
                        print(f"No loop found from path position {p} at ({sx},{sy}) in direction {sd}, obstacle at ({ox},{oy})")

                    break
            else:
                print(f"Error when seeking loop from path position {p} at ({sx},{sy}) in direction {sd}, obstacle at ({ox},{oy})")
                return (False, foundLoops)

            iterations += 1
            if iterations > 1000:
                if log_level >= 1:
                    print(f"Too many iterations to find loop from path position {p} at ({sx},{sy}) in direction {sd}, obstacle at ({ox},{oy})!")

                break

        # Reset map before next test
        mapData[oy][ox] = TILE_FLOOR

    return (True, foundLoops)


def play(input_data, day_part, log_level):

    #Initialize and read input

    mapData = []
    mapRow = None
    startPos = None
    startDir = None

    for line in input_data:
        mapRow = []

        for i, pos in enumerate(line.strip()):
            if pos == TILE_FLOOR:
                mapRow.append(pos)
            elif pos == TILE_OBSTACLE:
                mapRow.append(pos)
            else:
                mapRow.append(TILE_FLOOR)
                startPos = (i, len(mapData))
                startDir = 0
                print(f"Guard found at ({startPos[0]},{startPos[1]})")

        mapData.append(mapRow)

    if startPos == None:
        print(f"Error, guard was not found!")
        return

    height = len(mapData)
    width = len(mapData[0])
    
    tileID = startPos[1] * width + startPos[0]
    visitedMap = [False] * (width * height)
    visitedMap[tileID] = True
    path = [(tileID, startPos[0], startPos[1], startDir)]
    
    print("Day 6 begins!")

    walkUntilOutOfBounds(mapData, width, height, startPos, startDir, path, visitedMap, log_level)

    if day_part == 0 or day_part == 1:
    #Result tuple format is (success <bool>, result <int>)
        resultPart1 = getResultPart1(visitedMap)

        if (resultPart1[0]):
            print(f"Answer to Part 1 is {resultPart1[1]}\n")
        else:
            print("Unable to find answer to Part 1\n")

    if day_part == 0 or day_part == 2:
        #Result tuple format is (success <bool>, result <int>)
        resultPart2 = getResultPart2(mapData, width, height, startPos, startDir, path, visitedMap, log_level)

        if (resultPart2[0]):
            print(f"Answer to Part 2 is {resultPart2[1]}\n")
        else:
            print("Unable to find answer to Part 2\n")