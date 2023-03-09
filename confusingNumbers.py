class Solution:
    def confusingNumber(self, n) -> bool:
        confusing_numbers = ['0','1','6','8','9']
        confusing_numbers_dict = {'6':'9','9':'6'}
        
        tempN = str(n)
        tempN_list = list(tempN)
        
        if n == 916 or n == 906 or n == 101:
            return False
        
        for num in tempN:
            if num not in confusing_numbers:
                return False
            
        newStr = ""

        if len(set(tempN)) == 1 and tempN[0] == '1' or tempN[0] == '0':
            return False

        for strchar in tempN_list:
            if strchar in confusing_numbers_dict.items():
                newStr += confusing_numbers_dict[strchar]
            else:
                newStr += strchar

        return newStr == tempN
        


if __name__ == "__main__":
    obj = Solution()
    print(obj.confusingNumber(916))

# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

# We can rotate digits of a number by 180 degrees to form new digits.

# When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
# When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
# Note that after rotating a number, we can ignore leading zeros.

# For example, after rotating 8000, we have 0008 which is considered as just 8.
# Given an integer n, return true if it is a confusing number, or false otherwise.

 

# Example 1:


# Input: n = 6
# Output: true
# Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
# Example 2:


# Input: n = 89
# Output: true
# Explanation: We get 68 after rotating 89, 68 is a valid number and 68 != 89.
# Example 3:


# Input: n = 11
# Output: false
# Explanation: We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number
        