def Solution(S):

    array = [int(x) if x.isdigit() or (x[0] == '-' and x[1:].isdigit()) else x for x in S.split()]
    #print(array)

    stack = []

    for ele in array:
        if isinstance(ele, int):
            stack.append(ele)
            #print(f'stack: {stack}')
        else:
            if ele == "+":
                try:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1 + num2)
                except:
                    return -1
            elif ele == "-":
                try:
                    num1 = stack.pop()
                    num2 = stack.pop()
                except:
                    return -1
                stack.append(num1 - num2)
            elif ele == 'DUP':
                try:
                    num1 = stack.pop()
                    stack.append(num1)
                    stack.append(num1)
                except:
                    return -1
            elif ele == 'POP':
                stack.pop()

    ans = stack.pop()
    if ans >= 2 ** 20:
        return -1
    return ans


print(Solution("4 5 6 - 7 +"))
print(Solution("13 DUP 4 POP 5 DUP + DUP + -"))
print(Solution("5 6 + -"))
print(Solution("3 DUP 5 - -"))
print(Solution("1048575 DUP +"))
