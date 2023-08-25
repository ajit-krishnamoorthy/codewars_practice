#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1. (81-1-1-81)

#Example #2: An input of 765 will/should return 493625 because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

def square_digits(num):
    # Your code here
    numStr = str(num)
    for i in range(len(numStr)):
        temp = int(numStr[i])*int(numStr[i])
        if i == 0:
            final_str = str(temp)
        else: 
            final_str = final_str+str(temp)
    final_num = int(final_str)
    return final_num