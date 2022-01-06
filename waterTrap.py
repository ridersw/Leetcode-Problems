class Solution:
    def trap(self, height):

        if len(height) < 3:
            return 0
        
        maxLeft = [0]
        maxRight = [0]
        minLeftRight = []

        for swi in range(1, len(height)):
            maxLeft.append(max(height[:swi]))
            
        for swi in range(len(height)-1, 0, -1):
            maxRight.append(max(height[swi:]))

        maxRight = maxRight[::-1]

        for swi in range(len(maxLeft)):
            minLeftRight.append(min(maxLeft[swi], maxRight[swi]))

        print(f'minLeftRight: {minLeftRight}') 

        res = 0

        for swi in range(len(height)):
            res += max(minLeftRight[swi] - height[swi], 0)

        return res






if __name__ == "__main__":
    obj = Solution()

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    # height = [1,0,1]

    print(obj.trap(height))

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9