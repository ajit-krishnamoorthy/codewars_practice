def disemvowel(string_):
    newString = ""
    for i in range(len(string_)):
        ## Checking for each vovel in lower and upper case
        if string_[i] != "a" and string_[i] !="e" and string_[i] !="i" and string_[i] !="o" and string_[i] !="u" and string_[i] !="A" and string_[i] !="E" and string_[i] !="I" and string_[i] !="O" and string_[i] !="U":
            newString += string_[i]   #If it is not a vowel then copy to newString
    return newString