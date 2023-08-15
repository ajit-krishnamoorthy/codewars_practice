def high_and_low(numbers):
    # ...
    numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
    numbers_list = numbers.split(" ")
    largest = numbers_list[0]
    smallest = numbers_list[0]
    for i in range (len(numbers_list)):
        if int(numbers_list[i])<int(smallest):
            smallest = numbers_list[i]
        if int(numbers_list[i])>int(largest):
            largest = numbers_list[i]
    final_list_large = ' '.join(largest)
    final_list_small = ' '.join(smallest)
    final_list = final_list_large+' '+final_list_small
    return final_list