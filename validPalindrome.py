def validPalindrome(s):
	swi = 0
	swj = len(s) - 1
	
	while swi < swj:
		if s[swi] != s[swj]:
			tempi = s[:swi] + s[swi+1:]
			tempj = s[:swj] + s[swj+1:]
			
			if tempi != tempi[::-1] and tempj != tempj[::-1]:
				return False
			else:
				return True
				
		swi += 1
		swj -= 1
	
	return True
	
if __name__ == "__main__":
	print(validPalindrome(s = "aba"))
	print(validPalindrome(s = "abca"))
	print(validPalindrome(s = "abc"))
	print(validPalindrome(s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
	
	
#Given a string s, return true if the s can be palindrome after deleting at most one character from it.

#Example 1:

#Input: s = "aba"
#Output: true
#Example 2:

#Input: s = "abca"
#Output: true
#Explanation: You could delete the character 'c'.
#Example 3:

#Input: s = "abc"
#Output: false