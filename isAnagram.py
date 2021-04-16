from collections import Counter

def isAnagram(s, t):
	if len(s) != len(t):
		return False
		
	sCounter = dict(Counter(s))
	tCounter = dict(Counter(t))
	
	if sCounter == tCounter:
		return True
	return False
	
	
	
if __name__ == "__main__":
	#s = "anagram"
	#t = "nagaram"
	
	s = 'aacc'
	t = 'ccac'
	
	print(isAnagram(s, t))
	
#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

#Example 1:

#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:

#Input: s = "rat", t = "car"
#Output: false