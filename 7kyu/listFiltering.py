def filter_list(l):
    'return a new list with the strings filtered out'
    newList = []
    for i in l:
        if isinstance(i, int) and i >= 0:
            newList.append(i)
    return newList