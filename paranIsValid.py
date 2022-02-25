class Solution:
    def isValid(self, s):
        if len(s) <= 1:
            return False

        stack = []

        for ele in s:
            if ele == '[' or ele == '(' or ele == '{':
                stack.append(ele)
            else:
                if not stack:
                    return False
                if ele == ']':
                    popped_element = stack.pop()
                    if popped_element != '[':
                        return False
                elif ele == ')':
                    popped_element = stack.pop()
                    if popped_element != '(':
                        return False
                elif ele == '}':
                    popped_element = stack.pop()
                    if popped_element != '{':
                        return False

        return len(stack) == 0

if __name__ == "__main__":
    obj = Solution()

    print(obj.isValid(s = "()"))
    print(obj.isValid(s = "()[]{}"))
    print(obj.isValid(s = "(]"))
    print(obj.isValid(s = "){"))

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.