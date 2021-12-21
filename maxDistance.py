import math

class Solution:
    def maxDistance(self, arrays):

        minimumNumber = math.inf
        maximumNumber = -math.inf

        

        for swi in range(len(arrays)):
            if min(arrays[swi]) < minimumNumber:
                minimumNumber = min(arrays[swi])
                minimumIndex = swi

        for swi in range(len(arrays)):
            if max(arrays[swi]) > maximumNumber and swi != minimumIndex:
                maximumNumber = max(arrays[swi])

        return maximumNumber - minimumNumber


if __name__ == "__main__":
    obj = Solution()

    arrays = [[1,2,3],[4,5],[1,2,3]]
    arrays = [[1],[1]]
    arrays = [[1],[2]]
    arrays = [[1,4],[0,5]]

    print(obj.maxDistance(arrays))