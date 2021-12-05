def duplicateNumber(arr):
    dupli = None
    sum = 0

    arr.sort()

    for swi in range(len(arr)-1):
        if arr[swi] == arr[swi+1] and not dupli:
            dupli = arr[swi]
            sum -= arr[swi]
        sum += arr[swi]

    sum += arr[-1]
    print(f'duplicate: {dupli}')
    print(f'Sum: {sum}')

    for swi in range(1,len(arr)+1):
        sum -= swi

    return (dupli + abs(sum))
    



arr = [4,3,3,1]
arr = [2,2]
print(duplicateNumber(arr))