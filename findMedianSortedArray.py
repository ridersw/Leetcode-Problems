import math

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        
        length = len(nums1)/2

        print(f'length: {length}')

        if length - int(length) == 0:
            length = int(length)
            ans = (nums1[length] + nums1[length-1]c)/2
        else:
            length = int(length - 0.5)
            ans = nums1[length]

        return ans
       


if __name__ == "__main__":
    obj = Solution()
    print(obj.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
    print(obj.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106