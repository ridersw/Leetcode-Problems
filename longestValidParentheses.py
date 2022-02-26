class Solution:
    def longestValidParentheses(self, s):
        max_so_far, max_count = 0, 0

        array = []

        for ele in s:
            if ele == '(':
                array.append(max_count)
                max_count = 0
            elif ele == ")":
                if array:
                    max_count += array.pop() + 2
                    max_so_far = max(max_count, max_so_far)
                else:
                    max_count = 0

        return max_so_far



if __name__ == "__main__":
    obj = Solution()

    print(obj.longestValidParentheses(s = "(()"))
    print(obj.longestValidParentheses(s = ")()())"))
    print(obj.longestValidParentheses(s = ""))

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0