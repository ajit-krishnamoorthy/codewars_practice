def positive_sum(arr):
    # Your code here
    count = 0
    for i in range (len(arr)):
        if arr[i] > 0:
            count += arr[i]
        
    return count