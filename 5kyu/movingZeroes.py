#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
def move_zeros(lst):
    loopCount = lst.count(0)
    for i in range(loopCount):
        for j in range(len(lst)-1):
            if lst[j] == 0 and lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst