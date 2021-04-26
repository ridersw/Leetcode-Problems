def isIsomorphic(s, t):
	
	sourceDict = {}
	targetDict = {}
	
	for swi in range(len(s)):
		if s[swi] in sourceDict and sourceDict[s[swi]] != t[swi]:
			return False
		if t[swi] in targetDict and targetDict[t[swi]] != s[swi]:
			return False
		sourceDict[s[swi]] = t[swi]
		targetDict[t[swi]] = s[swi]
	
	return True
	
if __name__ == "__main__":
	s = "egg"
	t = "add"
	
	#s = "foo"
	#t = "bar"
	
	s = "paper"
	t = "title"
	
	#s = "badc"
	#t = "baba"
	print(isIsomorphic(s, t))
	
#Given two strings s and t, determine if they are isomorphic.

#Two strings s and t are isomorphic if the characters in s can be replaced to get t.

#All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

#Example 1:

#Input: s = "egg", t = "add"
#Output: true
#Example 2:

#Input: s = "foo", t = "bar"
#Output: false
#Example 3:

#Input: s = "paper", t = "title"
#Output: true