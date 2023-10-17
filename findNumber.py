class Solution:
    def findNumber(self, numbers):
        row = len(numbers)
        col = len(numbers[0])

        indices = []

        for swi in range(row):
            pass
        
        return indices


if __name__ == "__main__":
    obj = Solution()

    matrix = [
    [2, 5, 9],
    [6, 12, 15],
    [10, 12, 12]
]
    
    print(obj.findNumber(matrix))
