class Solution:
    def numFactoredBinaryTrees(self, arr):
        result = len(arr)

        # if len(arr) < 3:
        #     return result

        for swi in range(len(arr)):
            print(f'Root Node: {arr[swi]}')
            for swj in range(len(arr)):
                if (arr[swi] / arr[swj]) in arr:
                    print(f'Leaf Nodes are {arr[swj]} and {(arr[swi] // arr[swj])}')
                    result = result + 1

        return result


if __name__ == "__main__":
    obj = Solution()

    arr = [2,4,5,10]
    arr = [2,4]
    arr = [18,3,6,2]

    print(obj.numFactoredBinaryTrees(arr))

# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [2,4]
# Output: 3
# Explanation: We can make these trees: [2], [4], [4, 2, 2]
# Example 2:

# Input: arr = [2,4,5,10]
# Output: 7
# Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 

# Constraints:

# 1 <= arr.length <= 1000
# 2 <= arr[i] <= 109
# All the values of arr are unique.