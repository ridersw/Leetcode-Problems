def trial(matrix):
    side = 1
    area = 1
    swi = 0
    swj = 0
    flag = True
    while flag and (swi+side) <= len(matrix) and (swj+side) <= len(matrix[0]):
        print(f'For side: {side} and area: {area}')
        for sswi in range(swi, swi+side):
            for sswj in range(swj, swj+side):
                if matrix[sswi][sswj] == "0":
                    flag = False
                    break
        if flag:
            area = (side)**2
            side += 1
        else:
            break

    return area

matrix = [['1','1','0'],['1','1','1'],['1','1','1'],['1','1','1']]
print(trial(matrix))