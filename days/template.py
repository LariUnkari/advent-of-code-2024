"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""

def getResultPart1(data, log_level):
    return (False, "none")


def getResultPart2(data, log_level):
    return (False, "none")


def play(input_data, day_part, log_level):


    #Initialize and read input


    parsed_data = []


    print("Day template begins!")


    if day_part == 1:
        #Result tuple format is (success <bool>, result <string>)
        resultPart1 = getResultPart1(parsed_data, log_level)

        if (resultPart1[0]):
            print(f"Answer to Part 1 is {resultPart1[1]}")
        else:
            print("Unable to find answer to Part 1")


    if day_part == 2:
        #Result tuple format is (success <bool>, result <string>)
        resultPart2 = getResultPart2(parsed_data, log_level)

        if (resultPart2[0]):
            print(f"Answer to Part 2 is {resultPart2[1]}")
        else:
            print("Unable to find answer to Part 2")