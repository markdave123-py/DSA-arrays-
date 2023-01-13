#To determine the largest continous sum in an array

def largest_continuous_sum(arr):

    if len(arr) == 0:
        return 0

    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum+num, num)

        max_sum = max(max_sum, current_sum)

    return max_sum

