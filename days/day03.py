"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""

from ast import parse
import re

def getResultPart1(data, log_level):
    parsed_data = []

    for line in data:
        matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)
        for operation in matches:
            parsed_data.append((int(operation[0]), int(operation[1])))
            
    if log_level >= 1:
        print(f"Matches:\n{parsed_data}")

    sum = 0

    for operation in parsed_data:
        sum += operation[0] * operation[1]

    return (True, sum)


def getResultPart2(data, log_level):
    parsed_data = []

    for line in data:
        matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", line)

        for i, m in enumerate(matches):
            if m[0] != '':
                if log_level >= 2:
                    print(f"Found multiplication operation at match {i}")
                parsed_data.append(("mul", int(m[0]), int(m[1])))
            elif m[2] == 'do()':
                if log_level >= 2:
                    print(f"Found enabling operation at match {i}")
                parsed_data.append(("do()", True))
            elif m[3] == "don't()":
                if log_level >= 2:
                    print(f"Found disabling operation at match {i}")
                parsed_data.append(("don't()", False))
            
    if log_level >= 1:
        print(f"Matches:\n{parsed_data}")

    sum = 0

    enabled = True
    for operation in parsed_data:
        if operation[0] == "mul":
            if enabled:
                sum += operation[1] * operation[2]
        else:
            enabled = operation[1]

    return (True, sum)


def play(input_data, day_part, log_level):

    #Initialize and read input

    data = []
    for line in input_data:
        data.append(line)

    print("Day 3 begins!")

    if day_part == 0 or day_part == 1:
        #Result tuple format is (success <bool>, result <string>)
        resultPart1 = getResultPart1(data, log_level)

        if (resultPart1[0]):
            print(f"Answer to Part 1 is {resultPart1[1]}\n")
        else:
            print("Unable to find answer to Part 1\n")

    if day_part == 0 or day_part == 2:
        #Result tuple format is (success <bool>, result <string>)
        resultPart2 = getResultPart2(data, log_level)

        if (resultPart2[0]):
            print(f"Answer to Part 2 is {resultPart2[1]}\n")
        else:
            print("Unable to find answer to Part 2\n")