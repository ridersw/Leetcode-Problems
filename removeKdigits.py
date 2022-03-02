class Solution:
    def removeKdigits(self, num, k):

        numStack = []
        
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1
                
            numStack.append(digit)
            
            
        finalStack = numStack[:-k] if k else numStack
        
        return "".join(finalStack).lstrip('0') or "0"


if __name__ == "__main__":
    obj = Solution()

    print(obj.removeKdigits(num = "1432219", k = 3))
    print(obj.removeKdigits(num = "10200", k = 1))
    print(obj.removeKdigits(num = "10", k = 2))
    print(obj.removeKdigits(num = "112", k = 1))
    print(obj.removeKdigits(num = "0", k = 5))

# Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

# Example 1:

# Input: num = "1432219", k = 3
# Output: "1219"
# Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
# Example 2:

# Input: num = "10200", k = 1
# Output: "200"
# Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
# Example 3:

# Input: num = "10", k = 2
# Output: "0"
# Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

# Constraints:

# 1 <= k <= num.length <= 105
# num consists of only digits.
# num does not have any leading zeros except for the zero itself.