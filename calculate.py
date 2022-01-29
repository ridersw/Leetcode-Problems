class Solution:
    def calculate(self, s):
        stack = []
        pre_operator = "+"

        num = 0
        s += "+"

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)
            elif char == ' ':
                pass
            else:
                if pre_operator == "+":
                    stack.append(num)
                elif pre_operator == "-":
                    stack.append(-num)
                elif pre_operator == "*":
                    operant = stack.pop()
                    stack.append(int(operant) * num)
                else:
                    operant = stack.pop()
                    stack.append(int(operant) // num)
                num = 0
                pre_operator = char

        return sum(stack)





if __name__ == "__main__":
    obj = Solution()

    print(obj.calculate(s = "3+2*2"))

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.