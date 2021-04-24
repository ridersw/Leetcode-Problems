def maxPower(s):
	count, tempCount = 1, 1
	
	for swi in range(len(s)-1):
		print(f"Checking for {s[swi]} and {s[swi+1]}")
		if s[swi] == s[swi+1]:
			print(f"Match Found for {s[swi]} and {s[swi+1]}")
			tempCount += 1
			print(f"")
		else:
			count = max(count, tempCount)
			tempCount = 1
	count = max(count, tempCount)		
	return count
	
if __name__ == "__main__":
	s = "leetcode"
	s = "abbcccddddeeeeedcba"
	s = "triplepillooooow"
	s = "hooraaaaaaaaaaay"
	s = "cc"
	print(maxPower(s))
	
#Given a string s, the power of the string is the maximum length of a non-empty substring that contains only one unique character.

#Return the power of the string.

#Example 1:

#Input: s = "leetcode"
#Output: 2
#Explanation: The substring "ee" is of length 2 with the character 'e' only.
#Example 2:

#Input: s = "abbcccddddeeeeedcba"
#Output: 5
#Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
#Example 3:

#Input: s = "triplepillooooow"
#Output: 5