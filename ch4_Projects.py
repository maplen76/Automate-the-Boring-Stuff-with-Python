# Practice Projects
def commaCode(spam):
    a = ''
    for i in range(len(spam)):
        if i < len(spam) - 1:
            a = a + str(spam[i]) + ', '
        else:
            a = a + 'and ' + str(spam[i])
    return a

spam = ['apples', 'bananas', 'tofu', 'cats']
