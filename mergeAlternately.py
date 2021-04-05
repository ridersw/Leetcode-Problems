def mergeAlternately(word1, word2):
	word1 = list(word1)
	word2 = list(word2)
	resultantStr = ''
	
	pointer = 0
	
	while pointer < len(word1) or pointer < len(word2):
		if pointer < len(word1) and pointer < len(word2):
			resultantStr += word1[pointer]
			resultantStr += word2[pointer]
		elif pointer < len(word1):
			resultantStr += word1[pointer]
		else:# pointer < len(word2):
			resultantStr += word2[pointer]
			
		pointer += 1
		
	return resultantStr
	
if __name__ == "__main__":
	word1 = 'ab'
	word2 = 'pqrs'
	
	
	print(mergeAlternately(word1, word2))
	
	
#You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

#Return the merged string.


#Example 1:

#Input: word1 = "abc", word2 = "pqr"
#Output: "apbqcr"
#Explanation: The merged string will be merged as so:
#word1:  a   b   c
#word2:    p   q   r
#merged: a p b q c r

#Example 2:

#Input: word1 = "ab", word2 = "pqrs"
#Output: "apbqrs"
#Explanation: Notice that as word2 is longer, "rs" is appended to the end.
#word1:  a   b 
#word2:    p   q   r   s
#merged: a p b q   r   s