#Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#Examples:
#solution('abc', 'bc') # returns true
#solution('abc', 'd') # returns false

def solution(text, ending):
    sizeEnding = len(ending)
    reversedText = text[::-1]
    reversedEnding = ending[::-1]
    count = 0
    if len(text) >= len(ending):
        for i in range(len(ending)):
            if reversedText[i] != reversedEnding[i]:
                return False
    elif len(ending) > len(text):
        return False
    return True