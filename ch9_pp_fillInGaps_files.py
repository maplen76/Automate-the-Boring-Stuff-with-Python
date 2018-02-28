# Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, 
# in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt 
# but no spam002.txt). Have the program rename all the later files to close this gap.
# As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added.

## insert gaps into numbered files
import os, shutil, re

prefix = 'spam'
folder = 'D:\\PythonLab\\test'

# list files in the folder
files = os.listdir('D:\\PythonLab\\test')
files.sort()

dRegex = re.compile(r'.00(\d).')

number = 1
# rename files to fill the gaps by renaming files
for file in files:
    if not file.startswith(prefix) or not file.endswith('txt'):
        del files[files.index(file)]
print(files)

for i in range(len(files)):
    f1 = int(dRegex.search(files[i]).group(1))
    if i+1 == len(files):
        break
    else:
        f2 = int(dRegex.search(files[i+1]).group(1))
        if f1 + 1 == f2:
            continue
        else:
            n = f1
            while True:
                n = n + 1
                if n == f2:
                    break
                
                file_temp = prefix + '00' + str(n) + '.txt'
                path = os.path.join(folder, file_temp)
                newFile = open(path, 'w')
                newFile.close()
