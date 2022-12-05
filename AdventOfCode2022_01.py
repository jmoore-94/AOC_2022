# Reading in Data as .txt file
with open('Day01.txt', 'r') as inputFile:
    p_input = inputFile.read()


def ParseInput(puzzle):
    newPuzzle = []
    newPuzzle_Segment = []
    newPuzzle_Line = ''
    Elf_Number = 1
    for p in range(len(puzzle)):
        if puzzle[p] != '\n':
            newPuzzle_Line = newPuzzle_Line + puzzle[p]
            if p == (len(puzzle) - 1):
                newPuzzle_Segment.append(int(newPuzzle_Line))
                newPuzzle_Segment.insert(0, Elf_Number)
                newPuzzle.append(newPuzzle_Segment)
        elif puzzle[p] == '\n' and puzzle[p-1] == '\n':
            newPuzzle_Segment.insert(0, Elf_Number)
            newPuzzle.append(newPuzzle_Segment)
            Elf_Number = Elf_Number + 1
            newPuzzle_Segment = []
        else:
            newPuzzle_Segment.append(int(newPuzzle_Line))
            newPuzzle_Line = ''

    return newPuzzle


p_input = ParseInput(p_input)
Calories_List = []
for item in p_input:
    Calories = 0
    for i in range(len(item)):
        if i == 0:
            pass
        else:
            Calories = Calories + item[i]
    Calories_List.append(Calories)

# Part One (Find Max)
print (Calories_List)
print ('MAX: ' + str(max(Calories_List)))

# Part Two (Find top 3)
TopAmount = 3
TotalCalories = 0
Calories_List.sort(reverse=True)
Top_List = Calories_List[0:TopAmount]
for t in Top_List:
    TotalCalories = TotalCalories + t
print ('TOTAL: ' + str(TotalCalories))
