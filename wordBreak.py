def wordBreak(s, wordDict):
	
	if not s:
		return [[]]
	
	returnSentences = []
	
	for word in wordDict:
		if word == s[:len(word)]:
			newWord = s[len(word):]
			sentences = wordBreak(newWord, wordDict)
			finalSentences = [[word] + words for words in sentences]
			returnSentences.extend(finalSentences)
	
	#print(f"len(returnSentences): {len(returnSentences)}")
	#for swi in range(len(returnSentences)):
	#	print(returnSentences[swi])
		#returnSentences[swi] = " ".join(returnSentences[swi])
	return returnSentences
	
	
	
if __name__ == "__main__":
	print(wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
	
# a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

#Note that the same word in the dictionary may be reused multiple times in the segmentation.

#Example 1:

#Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
#Output: ["cats and dog","cat sand dog"]
#Example 2:

#Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
#Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
#Explanation: Note that you are allowed to reuse a dictionary word.
#Example 3:

#Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#Output: []
 

#Constraints:

#1 <= s.length <= 20
#1 <= wordDict.length <= 1000
#1 <= wordDict[i].length <= 10
#s and wordDict[i] consist of only lowercase English letters.
#All the strings of wordDict are unique.