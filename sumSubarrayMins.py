class Solution:
    def sumSubarrayMins(self, arr):
        result_array = []

        length = 1

        while length <= len(arr):
            temp = []
            for swi in range(len(arr)-length+1):
                temp.append(arr[swi:swi+length])

            result_array.extend(temp)
            temp = []
            length += 1

        print(result_array)

        sum = 0

        for array in result_array:
            print(f'for Array: {array} min is: {min(array)}')
            sum += min(array)

        return sum


if __name__ == "__main__":
    obj = Solution()

    arr = [3,1,2,4]
    arr = [11,81,94,43,3]

    print(obj.sumSubarrayMins(arr))

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