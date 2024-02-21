def isTrue(arr, sum):
    left = 0
    current_sum = 0
    min_len = float('inf')

    for r in range(len(arr)):
        current_sum += arr[r]

        while current_sum >= sum:
            min_len = min(min_len, r - left + 1)
            current_sum -= arr[left]
            left += 1

    
    if min_len != float('inf'):
        return min_len
    return 0

arr = [10, 20, 30, 40, 50, 60]
print(isTrue(arr, 120))