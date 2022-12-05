# Reading in Data as .txt file
with open('Day05.txt', 'r') as inputFile:
    p_input = inputFile.read()


def ParseInput(puzzle):
    newPuzzle_Segment = []
    newPuzzle_Line = ''
    for p in range(len(puzzle)):
        if puzzle[p] == '\n':
            newPuzzle_Segment.append(newPuzzle_Line)
            newPuzzle_Line = ''
        elif puzzle[p] != '\n':
            newPuzzle_Line = newPuzzle_Line + puzzle[p]
            if p == len(puzzle) - 1:
                newPuzzle_Segment.append(newPuzzle_Line)
    Rules_List = []
    Stack_Dictionary = {}
    for segment in range(len(newPuzzle_Segment)):
        # Get Rules
        if 'move' in newPuzzle_Segment[segment]:
            rule = newPuzzle_Segment[segment]
            rule = rule.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')
            Rules_List.append(rule)
        # Get Starting Stacks
        else:
            Row_Number = 0
            for s in range(len(newPuzzle_Segment[segment])):
                if (s + 1) % 2 == 0:
                    Row_Number = Row_Number + 1
                    if newPuzzle_Segment[segment][s] != ' ':
                        try:
                            int(newPuzzle_Segment[segment][s])
                        except ValueError:
                            Stack_Temp = [((Row_Number//2) + 1), newPuzzle_Segment[segment][s]]
                            if Stack_Temp[0] in Stack_Dictionary:
                                Stack_Dictionary[Stack_Temp[0]] = Stack_Dictionary[Stack_Temp[0]] + [Stack_Temp[1]]
                            else:
                                Stack_Dictionary[Stack_Temp[0]] = [Stack_Temp[1]]

    return Rules_List, Stack_Dictionary


def FollowRule(rule_to_follow, currentStack):
    boxes_to_move = int(rule_to_follow[0])
    stack = currentStack[int(rule_to_follow[1])]
    alteredStack = [stack[:boxes_to_move], stack[boxes_to_move:]]
    # Part One
    # if len(alteredStack[0]) > 1:
    #     alteredStack[0].reverse()
    currentStack[int(rule_to_follow[1])] = alteredStack[1]
    currentStack[int(rule_to_follow[2])] = alteredStack[0] + currentStack[int(rule_to_follow[2])]
    return currentStack


print(p_input)
Rule_List, StartingStack_Dictionary = ParseInput(p_input)

print(0, StartingStack_Dictionary)
for rule in range(len(Rule_List)):
    if rule == 0:
        newStack_Dictionary = FollowRule(Rule_List[rule], StartingStack_Dictionary)
        print(rule + 1, newStack_Dictionary)
    elif rule != 0:
        newStack_Dictionary = FollowRule(Rule_List[rule], newStack_Dictionary)
        print(rule + 1, newStack_Dictionary)

StackTops = ''
for key in newStack_Dictionary:
    StackTops = StackTops + newStack_Dictionary[key][0]
print(StackTops)
