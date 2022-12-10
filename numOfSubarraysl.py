class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        
        limit = k * threshold
        
        if len(arr) < k:
            return 0
        
        windowSum = sum(arr[0:k])
        if windowSum >= limit:
            count = count + 1
        
        for swi in range(len(arr)-k):
            windowSum = windowSum - arr[swi] + arr[swi+k]
            if windowSum >= limit:
                # print(f'Checking for {arr[swi:swi+k]}')
                count = count + 1
                
        return count

# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

# Example 1:

# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
# Output: 3
# Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
# Example 2:

# Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
# Output: 6
# Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
 

# Constraints:

# 1 <= arr.length <= 105
# 1 <= arr[i] <= 104
# 1 <= k <= arr.length
# 0 <= threshold <= 104
# Accepted
# 46,741
# Submissions
# 69,156