# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:25:40 2018

@author: jing.wang
"""

# python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - delete a keyword from the shelf file
#        py.exe mcb.pyw delete - delete all keywords from shelf file

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] not in list(mcbShelf.keys()):
            print(sys.argv[2] + ' not exist')
        else:
            del mcbShelf[sys.argv[2]]
            print(sys.argv[2] + ' was deleted')
   
elif len(sys.argv) == 2:
    # List Keywords and load content
    if sys.argv[1].lower() == 'delete':
        for k in list(mcbShelf.keys()):
            del mcbShelf[k]
        print('All of keys were deleted')
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(list(mcbShelf.keys()))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])  
mcbShelf.close()
