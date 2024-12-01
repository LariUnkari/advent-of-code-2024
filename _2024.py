
"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""


#Definitions

import os, importlib, modules.userInput

DAY_COUNT = len([f for f in os.listdir("days/") if f.startswith("day") == True])

def get_day_input():
    """Takes in user input for day choice"""

    print(f"Select day (1-{DAY_COUNT:d}), then press enter.\n"+
          "Give an empty input or 'exit' to end program\n")

    return input("Choose the day: ")

def get_data_input():
    """Takes in user input for data choice"""

    print(f"Type in 'test' to use testdata.txt, otherwise defaults to real data")

    INPUT = input("Select data: ")

    if INPUT == "test":
        return "testdata.txt"

    return "input{0:02d}.txt"

def get_program_and_input(day_input, data_input):
    """Returns a day solution program and input as tuple (module, input_file). If invalid, returns (None, None)"""
    
    mod = None
    modName = "day{0:02d}"

    try:
        value = int(day_input)

        if value < 1:
            print(f"Invalid day value {value} given!\n")
            return (None, None)
        elif value > DAY_COUNT:
            print(f"Day {value} has not been reached yet!\n")
            return (None, None)
        else:
            day = modName.format(value)
    except ValueError:
        print(f"Invalid input {day_input} given!")
        return (None, None)
    
    try:
        mod = importlib.import_module("."+day, package='days')
        print(f"Day {value} given, imported {day} module")
    except Exception as e:
        print(f"Day {value} given. Error importing module:\n{e}")
        return (None, None)

    filePath = "data/{0}".format(data_input.format(value))

    try:
        data = open(filePath, "r")
        print(f"Data {filePath} found")
    except FileNotFoundError:
        print(f"Unable to find input data file '{filePath}'!\n")
        return (None, None)

    return (mod, data)


#Program

DAY_INPUT = "0"

print("Advent of Code 2024 by Lari Unkari\n\n")

while True:
    DAY_INPUT = get_day_input()
    
    if len(DAY_INPUT) == 0 or DAY_INPUT.strip() == "exit":
        break
    
    print("")
    DATA_INPUT = get_data_input()
    
    print("")
    params = get_program_and_input(DAY_INPUT, DATA_INPUT)

    if params != None and params[0] != None:
        mod = params[0]
        if mod == None:
            print(f"No module found for {DAY_INPUT}")
            break

        input_file = params[1]
        if input_file == None:
            print(f"No input file found for {DAY_INPUT}")
            break
        
        part_input = modules.userInput.get_int_input_constrained("\nWhich part to run? 1-2 (defaults to 2): ", 1, 2, 2)

        log_level_input = modules.userInput.get_int_input("\nLog level (defaults to level zero): ", None)

        print("\n\n************************\n")
        mod.play(params[1], part_input[1], log_level_input[1] if log_level_input[0] else 0)
        print(f"\nModule {mod.__name__} program ended\n\n")

print("Goodbye and Merry Christmas 2024!")