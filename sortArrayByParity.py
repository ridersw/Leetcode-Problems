class Solution:
    def sortArrayByParity(self, nums):
        newArr = []
        
        for num in nums:
            if num % 2 == 0:
                newArr.append(num)
                
        for num in nums:
            if num % 2 != 0:
                newArr.append(num)
                
        return newArr

if __name__ == "__main__":
    obj = Solution()
    print(obj.sortArrayByParity(nums = [3,1,2,4]))