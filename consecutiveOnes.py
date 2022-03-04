class Solution:
    def consecutiveOnes(self, nums):
        nums = list(str(nums))
        print(f'nums: {nums}')

        curr_Ones, max_So_Far = 0, 0

        for swi in range(len(nums)):
            if nums[swi] == '1':
                curr_Ones += 1
                max_So_Far = max(max_So_Far, curr_Ones)
            else:
                max_So_Far = max(max_So_Far, curr_Ones)
                curr_Ones = 0

        return max_So_Far

if __name__ == "__main__":
    obj = Solution()

    print(obj.consecutiveOnes(nums = 1010101111110000))

#find consecutive 1's in the input number