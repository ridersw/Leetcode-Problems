arr = [1,2,3,4,5,6,7,8,9,10]
ans = False
for swi in range(len(arr)):
    if arr[swi] == 5:
        swi += 1
    print(arr[swi])