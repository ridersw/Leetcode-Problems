class Solution:
    def topKFrequent(self, nums, k):
        dict = {}

        if set(nums) == 1:
            return nums[0]
        
        for ele in nums:
            if ele in dict:
                dict[ele] += 1
            else:
                dict[ele] = 1
                
        print(f'dict: {dict}')
        sorted(dict, key=lambda k: dict[-1])
        print(f'dict: {dict}')
        ans = []
        
        for key, values in dict.items():
            ans.append(key)
            
        return ans[:k]

if __name__ == "__main__":
    obj = Solution()
    #print(obj.topKFrequent(nums = [1,1,1,2,2,3], k = 2))
    print(obj.topKFrequent(nums = [-1,-1], k = 1))

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 
# Constraints:

# 1 <= nums.length <= 105
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
        