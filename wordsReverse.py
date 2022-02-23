class Solution:
    def reverseWords(self, s):
        # s = "".join(s)
        # s = s.split()
        # s = s[::-1]
        # # s = "".join(s)
        # # s = list(s)
        # s = list(s)

        # print(f's: {s}')

        # return s

        # pointer1 = 0
        # pointer2 = len(s)-1

        # while pointer1 <= pointer2:
        #     s[pointer1], s[pointer2] = s[pointer2], s[pointer1]
        #     pointer1 += 1
        #     pointer2 -= 1

        # return s

        s.reverse()

        length = len(s)

        pointer1 = 0
        pointer2 = 0

        while pointer1 <= length:
            while pointer2 < length and s[pointer2] != ' ':
                pointer2 += 1
            pointer2 -= 1

            wpointer1 = pointer1
            wpointer2 = pointer2

            while wpointer1 < wpointer2:
                s[wpointer1], s[wpointer2] = s[wpointer2], s[wpointer1]
                wpointer2 -= 1
                wpointer1 += 1

            pointer1 = pointer2 + 2
            pointer2 = pointer1

        return s


if __name__ == "__main__":
    obj = Solution()

    s =  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]

    print(obj.reverseWords(s))

# Given a character array s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

# Your code must solve the problem in-place, i.e. without allocating extra space.

 

# Example 1:

# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
# Example 2:

# Input: s = ["a"]
# Output: ["a"]
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
# There is at least one word in s.
# s does not contain leading or trailing spaces.
# All the words in s are guaranteed to be separated by a single space.