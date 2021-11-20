class Solution:
    def jump(self, nums):
        countOfJumps = 0

        leftBound, rightBound = 0, 0

        while rightBound < len(nums)-1:
            farthest = 0

            for swi in range(leftBound, rightBound+1):
                farthest = max(farthest, swi + nums[swi])
            
            leftBound = rightBound+1
            rightBound = farthest
            countOfJumps += 1

        return countOfJumps

if __name__ == "__main__":
    nums = [2,3,1,1,4]
    nums = [2,3,0,1,4]

    obj = Solution()

    print(obj.jump(nums))

    