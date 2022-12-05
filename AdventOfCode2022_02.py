# Reading in Data as .txt file
with open('Day02.txt', 'r') as inputFile:
    p_input = inputFile.read()


# Rock = 1, Paper = 2, Scissors = 3
# Lose = 0, Win = 6, Draw = 3

def ParseInput(puzzle):
    newPuzzle = []
    newPuzzle_Segment = []
    newPuzzle_Line = ''
    for p in range(len(puzzle)):
        if puzzle[p] != '\n':
            newPuzzle_Line = newPuzzle_Line + puzzle[p]
            if p == len(puzzle) - 1:
                newPuzzle_Line_Split = SplitLine(newPuzzle_Line)
                newPuzzle_Segment.append(newPuzzle_Line_Split)
        elif puzzle[p] == '\n':
            newPuzzle_Line_Split = SplitLine(newPuzzle_Line)
            newPuzzle_Segment.append(newPuzzle_Line_Split)
            newPuzzle_Line = ''
    newPuzzle = newPuzzle_Segment
    return newPuzzle


def SplitLine(Line):
    newLine = Line.split(' ')
    return newLine


# Part One
# def Compare(Game):
#     Score = 0
#     You = Game[0]
#     Me = Game[1]
#     if Me == 'X':
#         Score = 1
#         if You == 'A':
#             Score += 3
#         elif You == 'B':
#             Score += 0
#         elif You == 'C':
#             Score += 6
#     elif Me == 'Y':
#         Score = 2
#         if You == 'A':
#             Score += 6
#         elif You == 'B':
#             Score += 3
#         elif You == 'C':
#             Score += 0
#     if Me == 'Z':
#         Score = 3
#         if You == 'A':
#             Score += 0
#         elif You == 'B':
#             Score += 6
#         elif You == 'C':
#             Score += 3
#     print(Score)
#     return Score


# Part Two
def Compare(Game):
    Score = 0
    You = Game[0]
    Me = Game[1]
    if Me == 'X':
        # Need to Lose
        Score = 0
        if You == 'A':
            # Throw Scissors
            Score += 3
        elif You == 'B':
            # Throw Rock
            Score += 1
        elif You == 'C':
            # Throw Paper
            Score += 2
    elif Me == 'Y':
        # Need to Tie
        Score = 3
        if You == 'A':
            # Throw Rock
            Score += 1
        elif You == 'B':
            # Throw Paper
            Score += 2
        elif You == 'C':
            # Throw Scissors
            Score += 3
    if Me == 'Z':
        # Need to Win
        Score = 6
        if You == 'A':
            # Throw Paper
            Score += 2
        elif You == 'B':
            # Throw Scissors
            Score += 3
        elif You == 'C':
            # Throw Rock
            Score += 1
    return Score


p_input = ParseInput(p_input)
print(p_input)


def RockPaperScissors(StrategyGuide):
    TotalScore = 0
    for item in StrategyGuide:
        TotalScore = TotalScore + Compare(item)
    return TotalScore


print(RockPaperScissors(p_input))
