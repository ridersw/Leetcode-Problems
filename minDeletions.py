from multiprocessing.sharedctypes import Value


class Solution:
    def minDeletions(self, s):
        
        dict = {}

        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        print(f'dict: {dict}')

        elements = []
        for key, values in dict.items():
            elements.append(values)

        elements.sort(reverse=True)
        print(f'elements: {elements}')

        count = 0

        if len(set(elements)) == len(elements):
            return count

        # for swi in range(len(elements)):
        #     try:
        #         elements.pop(0)
        #     except:
        #         pass
        #     if elements.count(elements[swi]) > 1:
        #         while elements.count(elements[swi]) > 1:
        #             elements[swi] -= 1
        #             count += 1

        # return count

        for swi in range(len(elements)):
            print(f'elements: {elements} checking for element: {elements[swi]}')
            if elements.count(elements[swi]) > 1:
                while elements.count(elements[swi]) > 1 and elements[swi] != 0:
                    elements[swi] -= 1
                    count += 1

        return count


if __name__ == "__main__":
    obj = Solution()

    s = "aaabbbcc"
    #s = "ceabaacb"
    #s = "aab"
    #s = "abcabc"
    s = "bbcebab"
    print(obj.minDeletions(s))

# A string s is called good if there are no two different characters in s that have the same frequency.

# Given a string s, return the minimum number of characters you need to delete to make s good.

# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

# Example 1:

# Input: s = "aab"
# Output: 0
# Explanation: s is already good.
# Example 2:

# Input: s = "aaabbbcc"
# Output: 2
# Explanation: You can delete two 'b's resulting in the good string "aaabcc".
# Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
# Example 3:

# Input: s = "ceabaacb"
# Output: 2
# Explanation: You can delete both 'c's resulting in the good string "eabaab".
# Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

# Constraints:

# 1 <= s.length <= 105
# s contains only lowercase English letters.