f = open(r'4/crossword.txt', 'r')
crossword = f.read()

lines = crossword.splitlines()

crossword_array = []
for i in range(len(lines)):
    crossword_array.append([])
    for j in range(len(lines)):
        crossword_array[i].append(lines[i][j])

array[i+1][j]
array[i][j+1]
array[i+1][j+1]
array[i-1][j-1]
array[i-1][j]
array[i][j-1]
array[i-1][j+1]
array[i+1][j-1]

def check_word(array, i, j):
    if array[i][j] == 'X':
        if
    #check up
    