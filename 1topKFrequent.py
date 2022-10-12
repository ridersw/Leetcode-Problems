class Solution:
    def topKFrequent(self, nums, k):
        dict = {}

        # if k == len(nums):
        #     return nums
        
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
         
        print(f'dict: {dict}')
        dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
        print(f'dict: {dict}')

        res = []

        for item, freq in dict:
            res.append(item)

        print(f'res: {res}')

        if k >= len(res):
            return res
        return res[:k]
        

if __name__ == "__main__":
    obj = Solution()
    print(obj.topKFrequent([-1,-1], 1))
    print(obj.topKFrequent([1,1,1,2,2,3], 2))
    print(obj.topKFrequent([4,1,-1,2,-1,2,3], 2))

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.