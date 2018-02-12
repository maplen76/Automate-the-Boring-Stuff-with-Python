def patternFinder(path, pat): 
    import re, os
    files = os.listdir(path)
    textRegex = re.compile(r'.txt$')
    print('Enter a pattern')
    patRegex = re.compile(pat)
    
    for i in files:
        if textRegex.search(i) == None:
            continue
        else:
            print('finding in ' + i)
            file = open(i)
            fileContent = file.read()
            file.close()
            
            if patRegex.findall(fileContent) == None:
                print('nothing found')
            else:
                print(patRegex.findall(fileContent))
                
