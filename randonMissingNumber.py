import random

class Solution:
    def randomNumber(self, n):
        
        arr = [1,2,3,5,6,7,8,9]

        for swi in range(1, n):
            arr.append(swi)

        missingNumber = random.choice(arr)
        print(f'missingNumber: {missingNumber}')
        arr.remove(missingNumber)

        return arr


if __name__ == "__main__":
    obj = Solution()

    print(obj.randomNumber(10))