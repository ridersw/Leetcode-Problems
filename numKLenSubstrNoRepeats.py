class Solution:
    def numKLenSubstrNoRepeats(self, s, k):
        if k > len(s):
            return 0

        s = list(s)
        count = 0

        for swi in range(len(s)-k + 1):
            if len(s[swi:swi+k]) == len(set(s[swi:swi+k])):
                count += 1

        return count



if __name__ == "__main__":
    obj = Solution()

    print(obj.numKLenSubstrNoRepeats(s = "havefunonleetcode", k = 5))
    print(obj.numKLenSubstrNoRepeats(s = "home", k = 5))


# Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 

# Example 1:

# Input: s = "havefunonleetcode", k = 5
# Output: 6
# Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
# Example 2:

# Input: s = "home", k = 5
# Output: 0
# Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
# 1 <= k <= 104