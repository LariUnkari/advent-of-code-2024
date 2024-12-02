"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""

from collections import Counter

def getResultPart1(left, right, log_level):
    distances = []
    r = -1
    d = -1

    for i, v in enumerate(left):
        r = right[i]
        d = abs(r - v)
        distances.append(d)
        
        if log_level >= 2:
            print(f"Distance between {v} and {r} is {d}")

    return (True, sum(distances))


def getResultPart2(left, right, log_level):
    occurrences = Counter(right)

    if log_level >= 1:
        print(f"Found {len(occurrences)} distinct locations on the right side")

    if log_level >= 2:
        for o in occurrences:
            print(f"{o} appears {occurrences[o]} times")

    scores = []
    num = -1

    for value in left:
        num = occurrences[value]
        
        if log_level >= 2:
            print(f"{value} from left appears {num} times on the right")
        elif log_level == 1 and num > 0:
            print(f"Found {value} from left {num} times on the right")

        scores.append(value * num)

    return (True, sum(scores))


def play(input_data, day_part, log_level):

    #Initialize and read input
    
    parsed_data = []
    left = []
    right = []
    line = ""
    
    for i in input_data:
        line = i.strip().split('   ')
        left.append(int(line[0]))
        right.append(int(line[1]))

    left.sort()
    right.sort()

    print("Day 1 begins!")
    
    if day_part == 0 or day_part == 1:
        #Result tuple format is (success <bool>, result <string>)
        resultPart1 = getResultPart1(left, right, log_level)

        if (resultPart1[0]):
            print(f"Answer to Part 1 is {resultPart1[1]}")
        else:
            print("Unable to find answer to Part 1")


    if day_part == 0 or day_part == 2:
        #Result tuple format is (success <bool>, result <string>)
        resultPart2 = getResultPart2(left, right, log_level)

        if (resultPart2[0]):
            print(f"Answer to Part 2 is {resultPart2[1]}")
        else:
            print("Unable to find answer to Part 2")