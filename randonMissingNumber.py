import random

class Solution:
    def randomNumber(self, n):
        
        arr = []

        for swi in range(1, n):
            arr.append(swi)

        missingNumber = random.choice(arr)
        print(f'missingNumber: {missingNumber}')
        arr.remove(missingNumber)

        return arr


if __name__ == "__main__":
    obj = Solution()

    print(obj.randomNumber(10))