#You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
def find_outlier(integers):
    evenCount = 0
    evenPosition = 0
    oddCount = 0
    oddPosition = 0
    for i in range(len(integers)):
        if integers[i] % 2 == 0:
            evenCount += 1
            evenPosition = i
        else:
            oddCount += 1
            oddPosition = i
    if evenCount == 1:
        return integers[evenPosition]
    else:
        return integers[oddPosition]
    return 