import os
os.chdir('d:\\PythonLab')

panda = open('panda.txt')  # open panda.txt file
pandaContent = panda.read() # read file
panda.close()
t = pandaContent.split('. A ')
wordlist = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']

for i in range(len(t)):
    word = t[i].split()
    for w in word:
        if w in wordlist:
            print('Enter ' + w.lower())
            temp = input()
            word[word.index(w)] = temp
        else:
            continue
    t[i] = ' '.join(word)   
t = '. A '.join(t)
print(t)

pandaNew = open('pandaNew.txt', 'w')
pandaNew.write(t)
pandaNew.close()


# =====================================================================================================================
# regular expression method
import os, re
os.chdir('d:\\PythonLab')

panda = open('panda.txt')  # open panda.txt file
pandaContent = panda.read() # read file
panda.close()

uRegex = re.compile(r'[A-Z]{2,}')
wordlist = uRegex.findall(pandaContent)
pandaContent = re.sub('[A-Z]{2,}', '%s', pandaContent)

for w in wordlist:
    if w[0].lower() in 'aeiou':
        c = 'an'
    else:
        c = 'a'
    print('Enter ' + c + ' ' + w.lower())
    temp = input()
    wordlist[wordlist.index(w)] = temp

pandaContentNew = pandaContent % tuple(wordlist)
print(pandaContentNew)

pandaNew = open('pandaNew.txt', 'w')
pandaNew.write(pandaContentNew)
pandaNew.close()
