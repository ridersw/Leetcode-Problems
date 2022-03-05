class Solution:
    def deleteAndEarn(self, nums):
        tempArr = [0] * (max(nums)+1)

        print(tempArr)

        for item in nums:
            tempArr[item] += item

        print(tempArr)

        dp = [0] * len(tempArr)

        dp[0] = tempArr[0]
        dp[1] = tempArr[1]

        for swi in range(2, len(tempArr)):
            dp[swi] = max(tempArr[swi-2] + tempArr[swi], tempArr[swi-1])

        print(f'dp: {dp}')
        return dp[-1]
        

if __name__ == "__main__":
    obj = Solution()
    #print(obj.deleteAndEarn(nums = [3,4,2]))
    print(obj.deleteAndEarn(nums = [2,2,3,3,3,4]))
