#Simple, given a string of words, return the length of the shortest word(s).
def find_short(s):
    # your code here
    sList = s.split()
    l = len(sList[0])
    for i in range(len(sList)):
        if len(sList[i]) < l:
            l = len(sList[i])
    return l # l: shortest word length