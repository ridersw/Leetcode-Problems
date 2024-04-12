class Solution:
    def maxArea(self, height) -> int:
        if len(height) < 2:
            return 0

        capacity = 0


        # bruteforce

        for swi in range(len(height)-1):
            for swj in range(swi+1, len(height)):
                print(f'Area: {height[swi]} and {height[swj]} Current Capacity: {capacity} New Capacity: {min(height[swi], height[swj]) * (swj-swi)} ')
                capacity = max(capacity, min(height[swi], height[swj]) * (swj-swi))

        return capacity
    

        # two pointer 

        pointer1 = 0
        pointer2 = len(height)-1

        while pointer1 < pointer2:
            capacity = max(min(height[pointer1], height[pointer2]) * (pointer2 - pointer1), capacity)

            if height[pointer1] < height[pointer2]:
                pointer1 += 1
            else:
                pointer2 -= 1

        return capacity

if __name__ == "__main__":
    obj = Solution()
    print(obj.maxArea(height =[1,8,6,2,5,4,8,3,7]))

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 

# Constraints:

# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104