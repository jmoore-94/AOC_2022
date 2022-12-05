# Reading in Data as .txt file
with open('Day03.txt', 'r') as inputFile:
    p_input = inputFile.read()


# Part One
def ParseInput(puzzle):
    newPuzzle = []
    newPuzzle_Line = ''
    for p in range(len(puzzle)):
        if puzzle[p] != '\n':
            newPuzzle_Line = newPuzzle_Line + puzzle[p]
            if p == len(puzzle) - 1:
                LineLength = len(newPuzzle_Line) / 2
                newPuzzle_Segment = newPuzzle_Line
                newPuzzle_Segment = [newPuzzle_Segment[:LineLength], newPuzzle_Segment[LineLength:]]
                newPuzzle.append(newPuzzle_Segment)
        elif puzzle[p] == '\n':
            LineLength = len(newPuzzle_Line) / 2
            newPuzzle_Segment = newPuzzle_Line
            newPuzzle_Segment = [newPuzzle_Segment[:LineLength], newPuzzle_Segment[LineLength:]]
            newPuzzle.append(newPuzzle_Segment)
            newPuzzle_Line = ''
    return newPuzzle


# Part Two
def ParseInput(puzzle):
    newPuzzle = []
    newPuzzle_Segment = []
    newPuzzle_Line = ''
    for p in range(len(puzzle)):
        if puzzle[p] != '\n':
            newPuzzle_Line = newPuzzle_Line + puzzle[p]
            if p == len(puzzle) - 1:
                newPuzzle_Segment.append(newPuzzle_Line)
        elif puzzle[p] == '\n':
            newPuzzle_Segment.append(newPuzzle_Line)
            newPuzzle_Line = ''
    # Clusters of 3
    for s in range(len(newPuzzle_Segment)):
        if (s + 1) % 3 == 0:
            newPuzzle.append(newPuzzle_Segment[s-2:s+1])
    return newPuzzle


def FindCommonType(LineList):
    CommonType = ''
    # Part One
    # for l in LineList[0]:
    #     for n in LineList[1]:
    #         if l == n:
    #             CommonType = l
    # Part Two
    for l in LineList[0]:
        for n in LineList[1]:
            for m in LineList[2]:
                if l == n and n == m:
                    CommonType = l
    return CommonType


def FindKey(val, user_Dictionary):
    for key, value in user_Dictionary.items():
        if value == val:
            return key
        else:
            pass


ValueDictionary = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}

print(p_input)
p_input = ParseInput(p_input)
print(p_input)
CountValues = 0
for item in p_input:
    Amount = 0
    CommonValue = FindCommonType(item)
    if CommonValue.isupper() is True:
        CommonValue = CommonValue.lower()
        Amount = 26
    CommonKey = FindKey(CommonValue, ValueDictionary)
    Amount = Amount + CommonKey
    CountValues = CountValues + Amount
print('TOTAL: ' + str(CountValues))
