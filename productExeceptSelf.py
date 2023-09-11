class Solution:
    def productExceptSelf(self, nums):
        tempVar = 1
        result = []

        if nums.count(0) == 0:
            for swi in range(len(nums)):
                tempVar = tempVar * nums[swi]
            
            for swi in range(len(nums)):
                result.append(int(tempVar // nums[swi]))

        elif nums.count(0) == 1:
            result = [0] * len(nums)
            zeroIndex = nums.index(0)

            for swi in range(len(nums)):
                if swi == zeroIndex:
                    continue
                tempVar = tempVar * nums[swi] 

            result[zeroIndex] = tempVar
             

        else:
            return [0] * len(nums)
        
        return result

if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,4]
    nums = [-1,1,0,-3,3]
    print(obj.productExceptSelf(nums))