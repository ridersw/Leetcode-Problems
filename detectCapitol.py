class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitolLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        count = 0
        
        for char in word:
            if char in capitolLetters:
                count += 1
                
        # print(f'count: {count}')
        # print(f'len(word): {len(word)}')
        if count == 0:
            return True
        
        if count == len(word):
            return True
        
        if count == 1 and word[0] in capitolLetters:
            return True
        
        return False
        

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.