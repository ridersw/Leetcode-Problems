class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(set(s)) == 1:
            return len(s)

        result = 0
        
        for swi in range(len(s)):
            tempChar = s[swi]
            count = k
            
            print(f'tempChar: {tempChar}')
            if swi + 1 >= k:
                pointer = swi-k+1
                length = 0
            else:
                pointer = swi+1
                length = 1
            for swj in range(pointer, len(s)):
                print(f'newChar: {s[swj]} and count: {count}')
                if s[swj] != tempChar:
                    if count > 0:
                        length += 1
                        count -= 1
                    else:
                        break
                else:
                    length += 1
            result = max(result, length)
                    
        return result

if __name__ == "__main__":
    obj = Solution()

    # print(obj.characterReplacement(s = "ABBB", k = 2))
    print(obj.characterReplacement(s = "AAAA", k = 0))

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only uppercase English letters.
# 0 <= k <= s.length