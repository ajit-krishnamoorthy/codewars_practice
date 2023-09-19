#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
def duplicate_count(text):
    newText = ''
    countDuplicate = 0
    lowerText = text.lower()
    for i in range(len(lowerText)):
        if lowerText.count(lowerText[i]) > 1:
            newText = newText+lowerText[i]
    newTextSet = set(newText)
    return len(newTextSet)