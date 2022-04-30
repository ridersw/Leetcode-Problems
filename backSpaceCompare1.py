class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        newS = []
        newT = []
        
        for char in s:
            if char != "#":
                newS.append(char)
            else:
                if newS:
                    del newS[-1]
                
        for char in t:
            if char != "#":
                newT.append(char)
            else:
                if newT:
                    del newT[-1]
        #print(f'newS: {newS} and newT: {newT}')    
        return newS == newT

# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

 

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
 

# Constraints:

# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.