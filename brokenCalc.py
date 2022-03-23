class Solution:
    def brokenCalc(self, startValue, target):
        
        res = 0

        while startValue != target:
            if (startValue * 2) <= target:
                startValue *= 2
            else:
                startValue -= 1
            res += 1

        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.brokenCalc(startValue = 2, target = 3))
    #print(obj.brokenCalc(startValue = 5, target = 8))
        