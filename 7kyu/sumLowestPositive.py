#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
def sum_two_smallest_numbers(numbers):
    indexSmall = 0
    smallest = numbers[0]+100
    secondSmallest = numbers[0]+100
    for i in range(len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            indexSmall = i
    for j in range(len(numbers)):
        if numbers[j] < secondSmallest and numbers[j] >= smallest and j !=indexSmall:
            secondSmallest = numbers[j]
    return smallest+secondSmallest