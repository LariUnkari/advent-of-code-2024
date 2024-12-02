"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""

def getResultPart1(data, log_level):
    safeCount = 0
    safe = False

    for identifier, report in enumerate(data):
        safe = validateReport(identifier, report, False, log_level)
            
        if safe:
            safeCount += 1

        if log_level >= 1:
            if safe:
                print(f"Report [{identifier}] '{report}' is safe, count now {safeCount}")
            else:
                print(f"Report [{identifier}] '{report}' is unsafe")   

    return (True, safeCount)


def getResultPart2(data, log_level):
    safeCount = 0
    safe = False

    for identifier, report in enumerate(data):
        safe = validateReport(identifier, report, True, log_level)
            
        if safe:
            safeCount += 1

        if log_level >= 1:
            if safe:
                print(f"Report [{identifier}] '{report}' is safe, count now {safeCount}")
            else:
                print(f"Report [{identifier}] '{report}' is unsafe")   

    return (True, safeCount)


def validateReport(identifier, report, allowDampening, log_level):
    if log_level >= 2:
        print(f"Report [{identifier}] {report} being validated!")

    length = len(report)
    safe = True
    a = 0
    b = 0
    diff = 0
    vector = 0
    constant = True
        
    i = 1
    while i < length:
        a = report[i-1]
        b = report[i]
        diff = b - a

        if diff > 0:
            if vector == 1:
                constant = True
            elif vector == -1:
                constant = False
            else:
                vector = 1
                constant = True
        elif diff < 0:
            if vector == 1:
                constant = False
            elif vector == -1:
                constant = True
            else:
                vector = -1
                constant = True

        if diff == 0:
            safe = False

            if log_level >= 2:
                print(f"Report [{identifier}] level[{i}] ({a} to {b}) = {diff} is unsafe due to no change!")
        elif not(constant):
            safe = False

            if log_level >= 2:
                print(f"Report [{identifier}] level[{i}] ({a} to {b}) = {diff} is unsafe due to direction change!")
        else:
            mag = abs(diff)

            if (mag >= 1 and mag <= 3):
                if log_level >= 3:
                    print(f"Report [{identifier}] level[{i}] ({a} to {b}) = {diff} is safe!")
            else:
                safe = False

                if log_level >= 2:
                    print(f"Report [{identifier}] level[{i}] ({a} to {b}) = {diff} is unsafe!")
                        
        i += 1

    if not(safe) and allowDampening:
        if log_level >= 1:
            print(f"Attempting dampening individual levels!")
        for index in range(length):
            if validateReport(f"{identifier}-{index}", report[:index] + report[index+1:], False, log_level):
                safe = True
                if log_level >= 1:
                    print(f"Report [{identifier}] dampened by removing level {report[index]} at index {index}")
                break

    return safe


def play(input_data, day_part, log_level):

    #Initialize and read input

    parsed_data = []

    for line in input_data:
        parsed_data.append(list(map(int, line.split(' '))))
        
    print("Day 2 begins!")
    
    if day_part == 0 or day_part == 1:
        #Result tuple format is (success <bool>, result <string>)
        resultPart1 = getResultPart1(parsed_data, log_level)

        if (resultPart1[0]):
            print(f"Answer to Part 1 is {resultPart1[1]}")
        else:
            print("Unable to find answer to Part 1")
            
    if day_part == 0 or day_part == 2:
        #Result tuple format is (success <bool>, result <string>)
        resultPart2 = getResultPart2(parsed_data, log_level)

        if (resultPart2[0]):
            print(f"Answer to Part 2 is {resultPart2[1]}")
        else:
            print("Unable to find answer to Part 2")