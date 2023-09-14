#The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.
def duplicate_encode(word):
    smallWord = word.lower()
    newWord = ''
    for i in range(len(smallWord)):
        if smallWord.count(smallWord[i]) == 1:
            newWord = newWord+"("
        else:
            newWord = newWord+")"
    return newWord