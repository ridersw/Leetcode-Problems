class Solution:
    def addDigits(self, num):
        
        length = len(str(num))

        while length > 1:
            # nums = map(int,str(num))
            nums = []
            for n in str(num):
                nums.append(int(n))
            num = sum(nums)
            length = len(str(num))

        return num


if __name__ == "__main__":
    obj = Solution()

    print(obj.addDigits(num = 12345))

# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 

# Constraints:

# 0 <= num <= 231 - 1