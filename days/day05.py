"""Advent of Code 2024 Solutions
Author: Lari Unkari
"""

def validatePagePair(rules, indexA, pageA, indexB, pageB, log_level):
    ruleAfter = f"{pageA}|{pageB}"
    ruleBefore = f"{pageB}|{pageA}"

    if ruleAfter in rules:
        if indexA < indexB:
            if log_level >= 3:
                print(f"Found rule after: {ruleAfter}, validated")
        else:
            if log_level >= 3:
                print(f"Found rule after: {ruleAfter}, INVALIDATED")

            return 1
    elif log_level >= 3:
        print(f"No rule after {ruleAfter} found, validated")
                        
    if ruleBefore in rules:
        if indexA > indexB:
            if log_level >= 3:
                print(f"Found rule before: {ruleBefore}, validated")
        else:
            if log_level >= 3:
                print(f"Found rule before: {ruleBefore}, INVALIDATED")
                
            return -1
    elif log_level >= 3:
        print(f"No rule before {ruleBefore} found, validated")

    return 0

def validateUpdate(rules, update, log_level):
    valid = True

    for p, page in enumerate(update):
        if log_level >= 2:
            print(f"Checking page {p} ({page})")

        for i in range(len(update)):
            if i == p:
                continue

            if not(validatePagePair(rules, i, update[i], p, page, log_level) == 0):
                valid = False
                break

        if not(valid):
            break

    return valid


def getResultPart1(rules, allUpdates, invalidUpdates, log_level):
    sum = 0

    for u, update in enumerate(allUpdates):
        if log_level >= 1:
            print(f"Checking update {u}: {update}")
            
        if validateUpdate(rules, update, log_level):
            mid = int(update[len(update) >> 1])

            if log_level >= 1:
                print(f"Update {u} has been validated, middle page value: {mid}")

            sum += mid
        else:
            if log_level >= 1:
                print(f"Update {u} has been INVALIDATED")

            invalidUpdates.append(update)

    return (True, sum)

def fixUpdate(rules, update, log_level):
    length = len(update)
    moves = [0] * length

    checkRange = None
    validation = 0
    otherPage = ''
    page = ''

    for p in range(length-1):
        page = update[p]
        checkRange = range(p + 1, length)

        if log_level >= 2:
            print(f"Checking page {p} ({page}) against pages {checkRange}")

        for i in checkRange:
            otherPage = update[i]
            validation = validatePagePair(rules, p, page, i, otherPage, log_level)

            if validation == 1:
                moves[p] += validation
                moves[i] -= validation
                if log_level >= 3:
                    print(f"Moving page {p} '{page}' up (now by {moves[p]}) and page {i} '{otherPage}' down (now by {moves[i]})")
            elif validation == -1:
                moves[p] -= validation
                moves[i] += validation
                if log_level >= 3:
                    print(f"Moving page {p} '{page}' down (now by {moves[p]}) and page {i} '{otherPage}' up (now by {moves[i]})")
            elif log_level >= 3:
                print(f"Page {p} '{page}' sits ok with page {i} '{otherPage}'")

    pageOrder = []
    fixedUpdate = [0] * length
    for n, value in enumerate(moves):
        pageOrder.append(n + value)
        fixedUpdate[n + value] = update[n]

    if log_level >= 2:
        print(f"New order of pages: {pageOrder}: {fixedUpdate}")

    return fixedUpdate

def getResultPart2(rules, invalidUpdates, log_level):
    sum = 0

    for u, update in enumerate(invalidUpdates):
        if log_level >= 1:
            print(f"Fixing update {u}: {update}")
            
        fixedUpdate = fixUpdate(rules, update, log_level)
        mid = int(fixedUpdate[len(fixedUpdate) >> 1])

        if log_level >= 1:
            print(f"Update {u} has been changed from {update} to {fixedUpdate}, middle page value: {mid}")

        sum += mid
        
    return (True, sum)


def play(input_data, day_part, log_level):

    #Initialize and read input

    rules = {}
    updates = None
    invalidUpdates = []

    for line in input_data:
        if updates == None:
            if line == '\n':
                updates = []

                if log_level >= 1:
                    print("Done adding rules, moving to updates")
            else:
                r = line.strip()
                rules[r] = True

                if log_level >= 3:
                    print(f"Rule added: {r}")
        else:
            u = line.strip().split(',')
            updates.append(u)
            
            if log_level >= 3:
                print(f"Update {len(updates)} added: {u}")

    print("Day 5 begins!")

    if day_part == 0 or day_part == 1:
        #Result tuple format is (success <bool>, result <string>)
        resultPart1 = getResultPart1(rules, updates, invalidUpdates, log_level)

        if (resultPart1[0]):
            print(f"Answer to Part 1 is {resultPart1[1]}, found {len(invalidUpdates)} invalid updates\n")
        else:
            print("Unable to find answer to Part 1\n")

    if day_part == 0 or day_part == 2:
        if len(invalidUpdates) == 0:
            getResultPart1(rules, updates, invalidUpdates, 0)

        #Result tuple format is (success <bool>, result <string>)
        resultPart2 = getResultPart2(rules, invalidUpdates, log_level)

        if (resultPart2[0]):
            print(f"Answer to Part 2 is {resultPart2[1]}\n")
        else:
            print("Unable to find answer to Part 2\n")