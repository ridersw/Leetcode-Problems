class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr1 = set(arr)

        for ele in arr:
            if (ele*2) in arr1:
                if ele == 0 and arr.count(0) > 1:
                    return True
                elif ele != 0:
                    return True

        return False
    
# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.
 

# Constraints:

# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103