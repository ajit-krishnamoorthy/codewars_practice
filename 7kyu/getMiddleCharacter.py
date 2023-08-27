def get_middle(s):
    wordLength = len(s)
    midPoint = int(wordLength/2)
    if wordLength % 2 ==0:
        #If the word has even letters, then return two middle characters
        return s[midPoint-1]+s[midPoint]
    else:
        #If the word has odd letters, then return one middle character
        return s[midPoint]