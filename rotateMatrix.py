from xxlimited import new


class Solution:
    def rotateMatrixBy90(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        newMatrix = [[0 for swi in range(rows)] for swj in range(cols)]

        print(f'newMatrix: {newMatrix}')

        for swi in range(rows):
            for swj in range(cols):
                newMatrix[swj][cols-swi-1] = matrix[swi][swj]

        return newMatrix




if __name__ == "__main__":
    obj = Solution()

    print(obj.rotateMatrixBy90(matrix = [[1,2,3],[4,5,6],[7,8,9]]))



# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]    