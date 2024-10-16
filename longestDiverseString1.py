class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        curra, currb, currc = 0,0,0

        total_iterations = a + b + c

        ans = ""

        for swi in range(total_iterations):
            if (a >= b and a >= c and curra != 2) or (a > 0 and (currb == 2 or currc == 2)):
                ans += 'a'
                curra += 1
                a -= 1
                currb = 0
                currc = 0
            elif (b >= a and b >= c and currb != 2) or (b > 0 and (curra == 2 or currc == 2)):
                ans += 'b'
                currb += 1
                curra = 0
                currc = 0
                b -= 1
            elif (c >= a and c >= b and currc != 2) or (c > 0 and (curra == 2 or currb == 2)):
                ans += 'c'
                currc += 1
                curra = 0
                currb = 0
                c -= 1

        return ans
            

        

if __name__ == "__main__":
    obj = Solution()
    print(f"answer: {obj.longestDiverseString(a = 1, b = 1, c = 7)}")

# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
 

# Constraints:

# 0 <= a, b, c <= 100
# a + b + c > 0