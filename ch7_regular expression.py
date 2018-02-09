# step to Regular Expression Matching
# 1. Import the regex module with import se
# 2. create a regex object with re.compile() function (put 'r' before the first quote to input raw string)
# 3. pass the string you want to search into the regex objects' search() method, will return a Match project
# 4. Call the Match objects' group() method to return the matched text

import se
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())
