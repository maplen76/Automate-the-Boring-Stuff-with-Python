# step to Regular Expression Matching
# 1. Import the regex module with import se
# 2. create a regex object with re.compile() function (put 'r' before the first quote to input raw string)
# 3. pass the string you want to search into the regex objects' search() method, will return a Match project
# 4. Call the Match objects' group() method to return the matched text

import se
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


# Practice Projects 1 strong password detection:
def password_detect():
    import re
    
    print('input a password to be detected')
    while True:
        password = input()
        if len(password) < 7:
            print ('Please make sure the password length more than 8')
            continue
        
        pwdUpperRegex = re.compile(r'[A-Z]')
        pwdLowerRegex = re.compile(r'[a-z]')
        pwdDigitRegex = re.compile(r'\d+')
        
        if pwdUpperRegex.search(password) != None and pwdLowerRegex.search(password) != None and pwdDigitRegex.search(password) != None:
            print('nice password ' + password)
            break
        elif pwdUpperRegex.search(password) == None:
            print('Please make sure at least 1 Upper case letter')
            continue
        elif pwdLowerRegex.search(password) == None:
            print('Please make sure at least 1 lower case letter')
            continue            
        elif pwdDigitRegex.search(password) == None:
            print('please make sure at least 1 digits included')
            continue

# Regex Version of strip()
def reg_strip(temp):
    import re
    stripRegex = re.compile(r'\s+')
    return stripRegex.sub('',temp) 
