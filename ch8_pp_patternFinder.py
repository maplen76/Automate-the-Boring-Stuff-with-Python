# Write a program that opens all .txt files in a folder and searches for any 
# line that matches a user-supplied regular expression. The results should be 
# printed to the screen.

def patternFinder(path): 
    import re, os
    files = os.listdir(path) # to list files in path
    textRegex = re.compile(r'.txt$') # creat regex object to find txt files
    print('Enter a pattern')
    
    pat = input()
    patRegex = re.compile(pat)
    
    for i in files:
        if textRegex.search(i) == None:
            continue
        else:
            print('finding in ' + i)
            file = open(i)
            fileContent = file.read()
            file.close()
            
            if patRegex.findall(fileContent) == []:
                print('nothing found')
            else:
                print(patRegex.findall(fileContent))
