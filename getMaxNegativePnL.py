# def getMaxNegativePnL(PnL):
#     sum = 0
#     count = 0
#     for swi in range(len(PnL)):
#         print(f'Current sum: {sum} checking for element: {PnL[swi]}')
#         if sum-(PnL[swi]) > 0:
#             print(f'can do')
#             count  += 1
#             sum -= PnL[swi]
#         else:
#             sum += PnL[swi]

#     return count

def getMaxNegativePnL(PnL):
    sum = 0
    count = 0
    for swi in range(len(PnL)):
        print(f'Current sum: {sum} checking for element: {PnL[swi]}')
        if PnL[swi] <= sum:
            count += 1
        else:
            sum += PnL[swi]
    return count

# Example usage:

# PnL1 = [5, 3, 1, 2]
# print(getMaxNegativePnL(PnL1))  # Output: 2

# PnL1 = [5, 3, 1, 2]
# print(getMaxNegativePnL(PnL1))  # Output: 2

# PnL2 = [1, 1, 1, 1, 1]
# print(getMaxNegativePnL(PnL2))  # Output: 2

PnL3 = [5, 2, 3, 5, 2, 3]
print(getMaxNegativePnL(PnL3))  # Output: 3