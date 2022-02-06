class Solution:
    def findMaxLength(self, nums):

        pointer1, pointer2 = 0, len(nums)

        while pointer1 < pointer2:

            if nums[pointer1:pointer2].count(1) == nums[pointer1:pointer2].count(0):
                return len(nums[pointer1:pointer2])

            if nums[pointer1:pointer2].count(1) > nums[pointer1:pointer2].count(0):
                if nums[pointer1] == 1:
                    pointer1 += 1
                else:
                    pointer2 -= 1
            else:
                if nums[pointer1] == 0:
                    pointer1 += 1
                else:
                    pointer2 -= 1

        return 0


if __name__ == "__main__":
    obj = Solution()

    nums = [0,1,0]
    #nums = [0,1]

    print(obj.findMaxLength(nums))