class Solution:
    def decodeString(self, s):
        stack  = []
        currNum = '0'
        currString = ""

        for char in s:
            if char == '[':
                stack.append(currString)
                stack.append(int(currNum))
                currString = ""
                currNum = '0'

            elif char == ']':
                num = stack.pop()
                prevString = stack.pop()
                currString = prevString + num*currString 

            elif char.isdigit():
                currNum += char
                
            else:
                currString += char

        return currString 


if __name__ == "__main__":
    obj = Solution()

    s = "3[a]2[bc]"
    # s = "3[a2[c]]"

    print(obj.decodeString(s))

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

# Example 1:

# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:

# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:

# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# Example 4:

# Input: s = "abc3[cd]xyz"
# Output: "abccdcdcdxyz"
 