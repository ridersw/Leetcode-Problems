class Solution:
    def minimumAverageDifference(self, nums):
        array = []
        leftSum = 0
        rightSum = sum(nums)
        length = len(nums)

        for swi in range(len(nums)):
            leftSum += nums[swi]
            rightSum -= nums[swi]

            leftSumAvg = leftSum // (swi+1)

            try:
                rightSumAvg = rightSum // (length - 1 - swi)
            except:
                rightSum = 0

            array.append(round(abs(leftSum - rightSum)))

        print(f'array: {array}')
        return array.index(min(array))

if __name__ == "__main__":
    obj = Solution()

    print(obj.minimumAverageDifference(nums = [2,5,3,9,5,3]))
    print(obj.minimumAverageDifference(nums = [0]))