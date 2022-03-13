class Solution:
    def isValid(self, s) -> bool:
        if len(s) <= 1:
            return False
        
        array = []
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                array.append(char)
            else:
                if not array:
                    return False
                popped_char = array.pop()
                
                if char == ')':
                    if popped_char != '(':
                        return False
                    
                if char == '}':
                    if popped_char != '{':
                        return False
                    
                if char == ']':
                    if popped_char != '[':
                        return False
                    
                    
        return len(array) == 0
                    

if __name__ == "__main__":
    obj = Solution()

    print(obj.isValid(s = "()[]{}"))

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