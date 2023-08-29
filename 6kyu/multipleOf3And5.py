def solution(number):
    if number < 0:
        return 0
    else:
        sumOfMultiples = 0
        numberLoopVar = number - 1  #Starting below the number
        while numberLoopVar > 0:
            #Check whether it is a multiple of 3 or 5
            if numberLoopVar % 3 == 0 or numberLoopVar % 5 == 0:
                sumOfMultiples = sumOfMultiples+numberLoopVar  #Add it to list
            numberLoopVar -= 1
        return sumOfMultiples