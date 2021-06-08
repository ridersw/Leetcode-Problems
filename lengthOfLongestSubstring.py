def lengthOfLongestSubstring(s):
	
	if not s:
		return 0
	
	finalLength = 1
	
	tempStr = ""
	
	for swi in range(len(s)):
		#print(f"Checking for {s[swi]} tempStr: {tempStr}")
		if s[swi] not in tempStr:
			tempStr += s[swi]
		else:
			finalLength = max(finalLength, len(tempStr))
			tempIndex = tempStr.index(s[swi])
		#	print(f"tempIndex: {tempIndex}")
			tempStr = tempStr[tempIndex+1:] + s[swi]
		#print(f"tempStr: {tempStr}")
	
	finalLength = max(finalLength, len(tempStr))
	return finalLength
	
if __name__ == "__main__":
	print(lengthOfLongestSubstring(s = "abcabcbb"))
	print(lengthOfLongestSubstring(s = "bbbbb"))
	print(lengthOfLongestSubstring(s = "pwwkew"))
	print(lengthOfLongestSubstring(s = ""))
	print(lengthOfLongestSubstring(s = "aab"))
	print(lengthOfLongestSubstring(s = "dvdf"))
	
	
#Given a string s, find the length of the longest substring without repeating characters.


#Example 1:

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:

#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
#Example 4:

#Input: s = ""
#Output: 0
 

#Constraints:

#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.