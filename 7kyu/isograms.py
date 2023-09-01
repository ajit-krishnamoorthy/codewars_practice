def is_isogram(string):
    #your code here
    if string == '':
        return True
    flag = 0
    for i in range(int(len(string))):
        for j in range(len(string)):
            if i != j:
                if string[i].lower() == string[j].lower():
                    flag = 1
    if flag == 0:
        return True
    else:
        return False