
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
    
    day = 0
    while day < 1:
        value = input("Choose the day: ")

        if len(value) == 0 or value.strip() == "exit":
            return 0

        try:
            day = int(value)

            if day < 1:
                print(f"Invalid day value {day} given!\n")
            elif day > DAY_COUNT:
                print(f"Day {day} has not been reached yet!\n")
            else:
                break
        except ValueError:
            print(f"Invalid input '{value}' given!")
            
    return day

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
    day = modName.format(day_input)
    
    try:
        mod = importlib.import_module("."+day, package='days')
        print(f"Day {day_input} given, imported {mod.__name__} module")
    except Exception as e:
        print(f"Day {day_input} given. Error importing module:\n{e}")
        return (None, None)

    filePath = "data/{0}".format(data_input.format(day_input))

    try:
        data = open(filePath, "r")
        print(f"Data {filePath} found")
    except FileNotFoundError:
        print(f"Unable to find input data file '{filePath}'!\n")
        return (None, None)

    return (mod, data)


#Program

print("Advent of Code 2024 by Lari Unkari\n\n")

while True:
    DAY_INPUT = get_day_input()
    
    if DAY_INPUT == 0:
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
        
        part_input = modules.userInput.get_int_input_constrained("\nWhich part to run? 2, 1, or 0 as in both (defaults to both): ", 0, 2, 0)
        if not(part_input[0]) or part_input[1] == 0:
            print("Running both parts")
        else:
            print(f"Running part {part_input[1]}")

        log_level_input = modules.userInput.get_int_input("\nLog level (defaults to level zero): ", None)

        print("\n\n************************\n")
        mod.play(params[1], part_input[1], log_level_input[1] if log_level_input[0] else 0)
        print(f"\nModule {mod.__name__} program ended\n\n")

print("Goodbye and Merry Christmas 2024!")