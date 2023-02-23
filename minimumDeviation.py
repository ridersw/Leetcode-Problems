import math
from heapq import heappop, heappush

class Solution:
    def minimumDeviation(self, nums) -> int:

        # if nums == [3, 5]:
        #     return 1

        # avg = sum(nums) / len(nums)
        # deviation = max(nums) - min(nums)
        # # print(f'Array Received: {nums} avg: {avg} deviation: {deviation}')
        
        # for swi in range(len(nums)):
        #     if nums[swi] % 2 == 0:
        #         #even
        #         # print(f'Found Even- {nums[swi]}')
        #         # print(f'abs(avg - (nums[swi]) // 2): {abs(avg - (nums[swi]) // 2)}')
        #         # print(f'abs(avg - (nums[swi]): {abs(avg - nums[swi])}')
        #         if abs(avg - (nums[swi]) // 2) <= abs(avg - (nums[swi])):
        #             nums[swi] = int(nums[swi] // 2)
        #     else:
        #         #odd
        #         if abs(avg - (nums[swi]) * 2) <= abs(avg - (nums[swi])):
        #             nums[swi] = int(nums[swi] * 2)

        # newDeviation = max(nums) - min(nums)
        # # print(f'Modified Array: {nums} newDeviation: {newDeviation}')
        # if newDeviation < deviation:
        #     deviation = self.minimumDeviation(nums)
        # return deviation

        evens = []
        minimum = math.inf
        
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num * 2)
                minimum = min(minimum, num*2)
                
        heapq.heapify(evens)
        
        # print(f'evens: {evens}')
        
        min_deviation = math.inf
        
        while evens:
            current_value = -heapq.heappop(evens)
            min_deviation = min(min_deviation, current_value - minimum)
            
            if current_value % 2 == 0:
                minimum = min(current_value // 2, minimum)
                heapq.heappush(evens, -current_value // 2)
            else:
                break
                
        return min_deviation


if __name__ == "__main__":
    obj = Solution()
    # print(obj.minimumDeviation(nums = [1,2,3,4]))
    # print(obj.minimumDeviation(nums = [4,1,5,20,3]))
    print(obj.minimumDeviation(nums = [2,10,8]))

# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
# Example 2:

# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
# Example 3:

# Input: nums = [2,10,8]
# Output: 3
 

# Constraints:

# n == nums.length
# 2 <= n <= 5 * 104
# 1 <= nums[i] <= 109