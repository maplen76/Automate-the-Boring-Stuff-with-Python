import os, shutil, re

prefix = 'spam'
folder = 'D:\\PythonLab\\test'

numRegex = re.compile(r'^.*?00(\d+)')

# list files in the folder
files = os.listdir('D:\\PythonLab\\test')
files.sort()

number = 1

# rename files to fill the gaps by renaming files
for file in files:
    if not file.startswith(prefix) or not file.endswith('txt'):
        continue
    
    file_temp = prefix + '00' + str(number) + '.txt'
    
    if file == file_temp:
        number = number + 1
        continue
    else:            
        path_old = os.path.join(folder,file)
        path_new = os.path.join(folder, file_temp)
        
        print(path_old + ' to ' + path_new)
        
        shutil.move(path_old, path_new)
        number = number + 1
