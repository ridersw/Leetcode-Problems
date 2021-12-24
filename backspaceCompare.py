class Solution:
    def backspaceCompare(self, s, t):
        tempS = []
        tempT = []

        for swi in range(len(s)):
            if s[swi] != "#":
                tempS.append(s[swi])
            elif s[swi] == "#" and tempS:
                tempS.pop()

        for swi in range(len(t)):
            if t[swi] != "#":
                tempT.append(t[swi])
            elif t[swi] == "#" and tempT:
                tempT.pop()
        
        print(f'tempS: {tempS}')
        print(f'tempT: {tempT}')

        return "".join(tempS) == "".join(tempT)


if __name__ == "__main__":
    obj = Solution()

    s = "ab#c"
    t = "ad#c"

    s = "ab##"
    t = "c#d#"

    s = "a#c"
    t = "b"

    print(obj.backspaceCompare(s, t))

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