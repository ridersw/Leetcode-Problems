class Solution:
    def sumSubarrayMins(self, arr):
        result = sum
        print(f'tempArr: {arr}')
        while len(arr) > 1:
            tempArr = []
            for swi in range(1, len(arr)):
                tempArr.append(min(arr[swi], arr[swi-1]))
            
            
            print(f'tempArr: {tempArr} result: {result} sum(arr): {sum(arr)}')
            arr = tempArr
            result = result + sum(arr)

        return result

        

if __name__ == "__main__":
    obj = Solution()

    print(obj.sumSubarrayMins(arr = [3,1,2,4]))

# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444
 

# Constraints:

# 1 <= arr.length <= 3 * 104
# 1 <= arr[i] <= 3 * 104