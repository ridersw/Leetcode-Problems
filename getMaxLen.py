class Solution:
    def getMaxLen(self, nums):
        positive = negative = 0

        result = 0

        for n in nums:
            if n == 0:
                positive = negative = 0
            elif n > 0:
                positive += 1
                negative = 0 if negative == 0 else negative+1
            else:
                temp = positive
                # positive = 0 if negative == 0 else negative+1
                if negative == 0:
                    positive = 0
                else:
                    positive = negative + 1
                negative = temp + 1

            result = max(positive, result)
        return result

if __name__ == "__main__":
    obj = Solution()
    nums = [[1,-2,-3,4],[0,1,-2,-3,-4],[-1,-2,-3,0,1], [-1,2],[1,2,3,5,-6,4,0,10]]

    for num in nums:
        print(obj.getMaxLen(num))

    