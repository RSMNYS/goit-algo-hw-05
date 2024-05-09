import random

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    i = 0
    upper_bound = 0
 
    while low <= high:
        i += 1
 
        mid = (high + low) // 2
        mid_value = arr[mid]
 
        if mid_value < x:
            low = mid + 1

        elif mid_value > x:
            upper_bound = mid_value
            high = mid - 1
        else:
            upper_bound = mid_value
            break
    if not upper_bound:
        return (i, -1)
    return (i, upper_bound)


def random_array(size):
    random_fractions = [random.uniform(0, 10) for _ in range(size)]
    sorted_fractions = sorted(random_fractions)
    return sorted_fractions

array_1 = random_array(10)
print(array_1)
print(binary_search(array_1, 5))
