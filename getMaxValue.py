def minimize_max(arr):
    n = len(arr)
    l, r = 1, max(arr)
    while l <= r:
        mid = (l + r) // 2
        prev = arr[0]
        count = 0
        for i in range(1, n):
            if arr[i] > prev:
                count += arr[i] - prev
                if count > mid:
                    break
            else:
                count -= prev - arr[i]
                if count < 0:
                    count = 0
            prev = arr[i]
        if count <= mid:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

print(minimize_max([1,5,7,6]))