def solving(days, k):

    # arr = []

    # for numDays in days:
    #     tempArr = list(range(1, numDays + 1))
    #     arr.extend(tempArr)

    # n = len(arr)
    # first_k = arr[:k-1]
    # arr.extend(first_k)

    # max_sum = float('-inf')
    # window_sum = 0

    # # Calculate the sum of the first window of size k
    # for i in range(k):
    #     window_sum += arr[i]

    # # Update the max_sum
    # max_sum = max(max_sum, window_sum)

    # # Slide the window and update the max_sum
    # for i in range(k, len(arr)):
    #     window_sum += arr[i] - arr[i - k]
    #     max_sum = max(max_sum, window_sum)

    # print(max_sum)

    arr = []

    for day in days:
        arr.append((day * (day + 1)) // 2)

    maxDay = max(days)
    maxDayIndex = days.index(maxDay)

    print(f'maxDay: {maxDay}')
    print(f'maxDayIndex: {maxDayIndex}')
    print(f'arr: {arr}')
    arrExtension = arr[:maxDayIndex]
    print(f'arrExtension: {arrExtension}')
    arr.extend(arrExtension)
    print(f'arr: {arr}')
    
    count = 0

    while True:
        if k - days[maxDayIndex] > 0:
            count += arr[maxDayIndex]
            k -= days[maxDayIndex]
        else:
            break

    
    count += sum(list(range(1, k + 1)))


    print(f'count: {count}')


solving([7,4,6,3,5], 8)
# solving([1,1], 2)