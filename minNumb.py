def Solution(A):
    arr = []

    A = str(A)

    for swi in range(len(A)):
        if A[swi] == '5':
            temp = A[:swi] + A[swi+1:]
            arr.append(int(temp))

    print(max(arr))



Solution(-5000)