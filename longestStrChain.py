def longestStrChain(words):
	
	count = 1
	maxCount = 1
	
	words.sort(key = len)
	words = words[::-1]
	print(f"words: {words}")
	
	for swi in range(len(words)-1):
		firstWord = words[swi]
		secondWord = words[swi+1]
		ans = True
		print(f"firstWord: {firstWord} and secondWord: {secondWord}")
		
		if len(firstWord) - 1 == len(secondWord):
			for swi in range(len(secondWord)):
				print(f"firstWord[swi]: {firstWord[swi]} and secondWord[swi]: {secondWord[swi]}")
				if firstWord[swi] != secondWord[swi]:
					print(f"firstWord[swi]: {firstWord[swi]} != secondWord[swi]: {secondWord[swi]}")
					#firstWord = firstWord.replace(firstWord[swi],"")
					firstWord = firstWord[:swi] + firstWord[swi+1:]
					print(f"Updated firstWord: {firstWord} and secondWord: {secondWord}")
					if firstWord == secondWord:
						print(f"firstWord == secondWord: {firstWord} == {secondWord}")
						count += 1
						print("================================================")
						print(f"Incrementing Count: {count}")
						print("================================================")
						ans = False
						break
					else:
						print(f"firstWord != secondWord: {firstWord} != {secondWord}")
						maxCount = max(maxCount, count)
						count = 1
						ans = False
						break
			
			if ans == True and firstWord[:-1] == secondWord:
				count += 1
				print("================================================")
				print(f"Incrementing Count: {count}")
				print("================================================")
		else:
			maxCount = max(maxCount, count)
			count = 1
	maxCount = max(maxCount, count)
	return maxCount
	
	
if __name__ == "__main__":
	#print(longestStrChain(words = ["xbc","xbfc"]))
	print(longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]))
	#print(longestStrChain(words = ["a","b","ba","bca","bda","bdca"]))
	
#Given a list of words, each word consists of English lowercase letters.

#Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

#A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

#Return the longest possible length of a word chain with words chosen from the given list of words.

#Example 1:

#Input: words = ["a","b","ba","bca","bda","bdca"]
#Output: 4
#Explanation: One of the longest word chain is "a","ba","bda","bdca".
#Example 2:

#Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
#Output: 5
 

#Constraints:

#1 <= words.length <= 1000
#1 <= words[i].length <= 16
#words[i] only consists of English lowercase letters.