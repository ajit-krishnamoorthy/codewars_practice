#Your task is to write a function maskify, which changes all but the last four characters into '#'.
def maskify(cc):
    lastFour = cc[-4:]   # Extracting last four characters of cc
    stringHash = '#'*(len(cc)-4)   # Getting a string of hash of length cc-4
    finalMasked = stringHash+lastFour  #Combining the strings
    return finalMasked