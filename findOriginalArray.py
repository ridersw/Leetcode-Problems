from typing import Counter


class Solution:
    def findOriginalArray(self, array):
        n = len(array)
        freq = Counter(array)
        array.sort()

        if n % 2 != 0:
            return []

        ans = []

        for swi, v in enumerate(array):
            if freq[v] > 0:
                if v == 0 and freq[0] < 2:
                    return []

                if v * 2 not in freq or freq[v*2] == 0:
                    return []

                freq[v] -= 1
                freq[v*2] -= 1
                ans.append(v)

        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.findOriginalArray(array = [1,3,4,2,6,8]))
    print(obj.findOriginalArray(array =  [6,3,0,1]))
    print(obj.findOriginalArray(array = [0,3,2,4,6,0]))

# An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

# Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

# Example 1:

# Input: changed = [1,3,4,2,6,8]
# Output: [1,3,4]
# Explanation: One possible original array could be [1,3,4]:
# - Twice the value of 1 is 1 * 2 = 2.
# - Twice the value of 3 is 3 * 2 = 6.
# - Twice the value of 4 is 4 * 2 = 8.
# Other original arrays could be [4,3,1] or [3,1,4].
# Example 2:

# Input: changed = [6,3,0,1]
# Output: []
# Explanation: changed is not a doubled array.
# Example 3:

# Input: changed = [1]
# Output: []
# Explanation: changed is not a doubled array.
 

# Constraints:

# 1 <= changed.length <= 105
# 0 <= changed[i] <= 105