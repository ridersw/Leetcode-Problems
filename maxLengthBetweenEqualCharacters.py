def maxLengthBetweenEqualCharacters(s):
	length = -1
	s = list(s)
	for ele in s:
		if s.count(ele) > 1:
			newString = s.copy()
			newString = newString[::-1]
			index1 = s.index(ele)
			index2 = len(s) - newString.index(ele) - 2
			if length < (index2 - index1):
				length = index2 - index1

	return length
	
	
if __name__ == "__main__":
	s = "abca"
	#s = "aa"
	#s = "cbzxy"
	#s = "cabbac"
	#s = "mgntdygtxrvxjnwksqhxuxtrv"
	
	print(maxLengthBetweenEqualCharacters(s))
	
#Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

#A substring is a contiguous sequence of characters within a string.

#Example 1:

#Input: s = "aa"
#Output: 0
#Explanation: The optimal substring here is an empty substring between the two 'a's.
#Example 2:

#Input: s = "abca"
#Output: 2
#Explanation: The optimal substring here is "bc".
#Example 3:

#Input: s = "cbzxy"
#Output: -1
#Explanation: There are no characters that appear twice in s.
#Example 4:

#Input: s = "cabbac"
#Output: 4
#Explanation: The optimal substring here is "abba". Other non-optimal substrings include "bb" and "".