from collections import Counter

class Solution:
    
    def checkInclusion(self, s1, s2):
        # s1 = list(s1)
        # s1.sort()
        # s1 = "".join(s1)

        # s2 = list(s2)

        # length = len(s1)

        # for swi in range(len(s2)):
        #     if s2[swi] in s1:
        #         temp = s2[swi:swi+length]
        #         temp.sort()
        #         temp = "".join(temp)

        #         if temp == s1:
        #             return True

        # return False

        d1 = Counter(s1)
        length = len(s1)
        print(f'd1: {d1}')

        for swi in range(len(s2)):
            sub = s2[swi:swi+length]
            d2 = Counter(sub)

            if d1 == d2:
                return True

        return False

if __name__ == "__main__":
    obj = Solution()

    print(obj.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
    print(obj.checkInclusion(s1 = "ab", s2 = "eidboaoo"))
    print(obj.checkInclusion(s1 = "s", s2 = "shashiraj"))

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.