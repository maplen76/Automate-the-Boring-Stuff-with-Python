# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:15:41 2018

@author: jing.wang
"""
#! Python3
# selectiveCopy.py - To copy files with expected extention into another new folder

import os, shutil

def selectiveCopy(folder, extention, newFolder):
    if not os.path.exists(newFolder):
        os.makedirs(newFolder)
    
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if not filename.endswith(extention):
                continue
            
            # to get full path to a file directory in dirpath
            src = os.path.join(foldername, filename)
            print(src)
            shutil.copy(src, newFolder)
        
        
selectiveCopy('F:\\Console_WOF\\RApps', 'png', 'F:\\Console_WOF\\RApps\\test')
