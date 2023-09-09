#Given an array of integers, find the one that appears an odd number of times.
def find_it(seq):
    numDict = {}   #Creating a dictionary to store the values
    for i in range(len(seq)):
        # The individual number in seq will be the keys and amount of times it is repeated will be values
        if seq[i] in numDict.keys():
            numDict[seq[i]] +=1
        else:
            numDict[seq[i]] = 1
    keyList = list(numDict.keys())
    valueList = list(numDict.values())
    position = 0
    # Finding the key that is repeated odd number of times
    for i in range(len(valueList)):
        if valueList[i] % 2 == 1:
            position = i
    return keyList[position]