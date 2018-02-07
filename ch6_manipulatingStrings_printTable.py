# Write a function named printTable() that takes a list of lists of strings 
# and displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings. 
# For example, the value could look like this:
# Practice Project: Table Printer
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# define mx_width to find the max width of each list
def mx_width(t):
    mx = 0
    for i in range(len(t)):
        mx = max(mx, len(t[i]))
    return mx

# define c_t to transpose the list and print the output
def c_t(tableData):
    temp = []
    for j in range(4):
        t = []
        for i in range(len(tableData)):
            t.append(tableData[i][j])
        temp.append(t)        
    for i in range(len(temp)):
        print(' '.join(temp[i]))

def printTable(tableData):    
    for i in range(len(tableData)):
        mx = int(mx_width(tableData[i]))
        for j in range(len(tableData[i])):
            tableData[i][j] = tableData[i][j].rjust(mx)          
    return c_t(tableData)
