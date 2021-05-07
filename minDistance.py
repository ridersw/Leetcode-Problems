def minDistance(word1, word2):
	count = 0
	
	if word2 in word1:
		return len(word1) - len(word2)
	elif word1 in word2:
		return len(word2) - len(word1)
	else:
		if len(word1) == len(word2):
			for swi in range(len(word1)):
				if word1[swi] != word2[swi]:
					count += 1
					
		return count
	
	dict = {}
	
	for character in word1:
		if character in dict:
			dict[character] += 1
		else:
			dict[character] = 1
			
	for character in word2:
		if character in  dict:
			dict[character] -= 1
		else:
			dict[character] = 1
			
	for key, values in dict.items():
		count += abs(values)
		
	return count
	
	
	
if __name__ == "__main__":
	print(minDistance(word1 = "sea", word2 = "eat"))
	print(minDistance(word1 = "sea", word2 = "aet"))
	print(minDistance(word1 = "leetcode", word2 = "etco"))
	
#Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

#In one step, you can delete exactly one character in either string.

#Example 1:

#Input: word1 = "sea", word2 = "eat"
#Output: 2
#Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
#Example 2:

#Input: word1 = "leetcode", word2 = "etco"
#Output: 4
	