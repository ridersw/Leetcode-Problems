def areAlmostEqual(s1, s2):

	if s1 == s2:
		return True
	
	swapIndex = []
	s1 = list(s1)
	s2 = list(s2)
	
	for swi in range(len(s1)):
		if s1[swi] != s2[swi]:
			swapIndex.append(swi)
			if len(swapIndex) >= 2:
				break
	
	if len(swapIndex) == 2:
		s1[swapIndex[0]], s1[swapIndex[1]] = s1[swapIndex[1]], s1[swapIndex[0]]
	
	if "".join(s1) == "".join(s2):		
		return True
	else:
		return False
	
if __name__ == "__main__":
	s1 = "aa"
	s2 = "ac"
	#s1 = "abcd"
	#s2 = "abdc"
	print(areAlmostEqual(s1, s2))
	
	
#You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

#Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

#Example 1:

#Input: s1 = "bank", s2 = "kanb"
#Output: true
#Explanation: For example, swap the first character with the last character of s2 to make "bank".

#Example 2:

#Input: s1 = "attack", s2 = "defend"
#Output: false
#Explanation: It is impossible to make them equal with one string swap.

#Example 3:

#Input: s1 = "kelb", s2 = "kelb"
#Output: true
#Explanation: The two strings are already equal, so no string swap operation is required.

#Example 4:

#Input: s1 = "abcd", s2 = "dcba"
#Output: false

#Constraints:

#1 <= s1.length, s2.length <= 100
#s1.length == s2.length
#s1 and s2 consist of only lowercase English letters.