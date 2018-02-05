# Practice Projects
def commaCode(spam):
    a = ''
    for i in range(len(spam)):
        if i < len(spam) - 1:
            a = a + str(spam[i]) + ', '
        else:
            a = a + 'and ' + str(spam[i])
    return a

spam = ['apples', 'bananas', 'tofu', 'cats']



# Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def paste0(spam):
    a = ''
    for i in range(len(spam)):
        a = a + str(spam[i])
    return a

def gridP(grid):    
    for n in range(6):
        a = ''
        for i in range(len(grid)):
            a = a + grid[i][n]
        print(a)
