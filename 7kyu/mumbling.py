#This time no story, no theory. The examples below show you how to write function accum:

#Examples:
#accum("abcd") -> "A-Bb-Ccc-Dddd"
#accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accum(s):
    # your code
    sList = [i for i in s]  #Adding the string in a list
    for i in range(len(sList)):
        sList[i] = sList[i].upper()   #Making the first instance upper case
        sList[i]+=sList[i].lower()*i  #Adding the other instances in lower case based on the count
    finalS = '-'.join(sList)
    return finalS