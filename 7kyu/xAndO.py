#Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
def xo(s):

    countX = 0
    countO = 0
    for i in range(len(s)):
        if s[i].lower() == 'x':
            countX +=1
        if s[i].lower() == 'o':
            countO +=1       
    if countO == countX:
        return True
    else:
        return False