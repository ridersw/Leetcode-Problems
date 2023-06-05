class Solution:
    def stringPatterns(self, wordLen, maxVowels):
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = [chr(ord('a') + i) for i in range(26) if chr(ord('a') + i) not in vowels]
        patterns = ['C', 'V']
        wordCount = 0
        
        def backtrack(currWord, currVowelCount):
            nonlocal wordCount
            
            if len(currWord) == wordLen:
                wordCount += 1
                return
            
            for pattern in patterns:
                if pattern == 'V':
                    if currVowelCount < maxVowels:
                        for vowel in vowels:
                            backtrack(currWord + vowel, currVowelCount + 1)
                else:
                    for consonant in consonants:
                        backtrack(currWord + consonant, 0)
        
        backtrack('', 0)
        return wordCount


if __name__ == "__main__":
    obj = Solution()
    print(obj.stringPatterns(2, 1))