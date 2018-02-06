# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:36:41 2018

@author: jing.wang
"""

#! python3
# pw.py - An insecure password locker program.


PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

import pyperclip 
import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1] # sys.argv is a list

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account )
