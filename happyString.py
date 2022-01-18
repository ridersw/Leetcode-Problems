class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        s = []
        
        items = [[a, 'a'],[b, 'b']]
        
        while True:
            items.sort()
            
            if len(s) >= 2 and s[-1] == s[-2] == items[1][1]:
                swi= 0
            else:
                swi = 1
                
            if items[swi][0]:
                s.append(items[swi][1])
                items[swi][0] -= 1
            else:
                break
                
        return "".join(s)
            
# Given two integers a and b, return any string s such that:

# s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
# The substring 'aaa' does not occur in s, and
# The substring 'bbb' does not occur in s.
 

# Example 1:

# Input: a = 1, b = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# Example 2:

# Input: a = 4, b = 1
# Output: "aabaa"
 

# Constraints:

# 0 <= a, b <= 100
# It is guaranteed such an s exists for the given a and b.