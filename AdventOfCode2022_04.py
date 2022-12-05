# Reading in Data as .txt file
with open('Day04.txt', 'r') as inputFile:
    p_input = inputFile.read()


def ParseInput(puzzle):
    newPuzzle = []
    newPuzzle_Segment = []
    newPuzzle_Line = ''
    for p in range(len(puzzle)):
        if puzzle[p] != '\n':
            newPuzzle_Line = newPuzzle_Line + puzzle[p]
            if p == len(puzzle) - 1:
                newPuzzle_Segment.append(newPuzzle_Line.split(','))
        elif puzzle[p] == '\n':
            newPuzzle_Segment.append(newPuzzle_Line.split(','))
            newPuzzle_Line = ''
    # Fill out the sections
    for segment in newPuzzle_Segment:
        Section_List = []
        for s in segment:
            Section = s.split('-')
            Section = list(range(int(Section[0]), int(Section[-1]) + 1, 1))
            Section_List.append(Section)
        newPuzzle.append(Section_List)
    return newPuzzle


def FindContainedSections(Section):
    Section_Intersection = (list(set(Section[0]).intersection(set(Section[1]))))
    Section_Intersection.sort()
    # Part One
    # if Section_Intersection == Section[0] or Section_Intersection == Section[1]:
    #     return True
    # else:
    #     return False
    #
    # Part Two
    if len(Section_Intersection) > 0:
        return True
    else:
        return False


print(p_input)
p_input = ParseInput(p_input)

Tally = 0
for p in p_input:
    Contained = FindContainedSections(p)
    if Contained is True:
        Tally += 1
    elif Contained is False:
        pass
print(Tally)
