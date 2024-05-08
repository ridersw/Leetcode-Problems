class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ('Q','W','E','R','T','Y','U','I','O','P')
        row2 = ('A','S','D','F','G','H','J','K','L')
        row3 = ('Z','X','C','V','B','N','M')
        answer = []
        for word in words:
            tempWord = list(word)
            tempArr = []

            for w in tempWord:
                if w.upper() in row1:
                    tempArr.append('r1')
                elif w.upper() in row2:
                    tempArr.append('r2')
                else:
                    tempArr.append('r3')

            if len(set(tempArr)) == 1:
                answer.append(word)

        return answer
        
# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

 

# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
 

# Constraints:

# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 