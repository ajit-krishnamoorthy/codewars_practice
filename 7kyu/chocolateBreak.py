def break_chocolate(n, m):
    ## Checking for invalid inputs or inputs not needing breaks
    if n==1 and m==1:
        return 0
    if n<=0 or m<=0:
        return 0
    ## The number of breaks needed is nxm-1 for all cases of n and m
    numBreaks = (n*m)-1
    return numBreaks