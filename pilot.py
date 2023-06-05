class Solution:
    def travelPath(self, xCoordinate_size, xCoordinates, yCoordinate_size, yCoordinates):

        # max_rows = max(xCoordinates)
        # max_cols = max(yCoordinates)

        # coord = [[xCoordinates[i], yCoordinates[i]] for i in range(len(yCoordinates))]

        # matrix = [[0 for j in range(max_cols)] for i in range(max_rows)]

        # for swi in range(max_rows):
        #     for swj in range(max_cols):
        #         if [swi, swj] in coord:
        #             matrix[swi][swj] = 1

        # max_sum = 0

        # #for rows

        # row_sums = [sum(row) for row in matrix]
        # print(f'row_sums: {row_sums}')
        # max_row_index = row_sums.index(max(row_sums))

        # col_sums = [sum(col) for col in zip(*matrix)]
        # print(f'col_sums: {col_sums}')

        # # Find the index of the column with the maximum sum
        # max_col_index = col_sums.index(max(col_sums))

        # return max(max_row_index, max_col_index)

        x_dict = {}
        y_dict = {}

        for ele in xCoordinates:
            if ele not in x_dict:
                x_dict[ele] = 0
            x_dict[ele] += 1

        for ele in yCoordinates:
            if ele not in y_dict:
                y_dict[ele] = 0
            y_dict[ele] += 1

        # print(f'x: {x_dict.values()}')
        # print(f'y: {y_dict.values()}')
        return max(max(x_dict.values()), max(y_dict.values()))

if __name__ == "__main__":
    obj = Solution()
    xCoordinate_size = 5
    xCoordinates = [2, 3, 2, 4, 2]
    yCoordinate_size = 5
    yCoordinates = [2, 2, 6, 5, 8]

    print(obj.travelPath(xCoordinate_size, xCoordinates, yCoordinate_size, yCoordinates))