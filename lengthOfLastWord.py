def lengthOfLastWord(s):
	#if not s: 
	#	return 0
		
	#s = s.split(" ")
	#print(f"s: {s}")
	#length = len(s)
	#return len(s[length-1])
	
	s = s.split()
	if s == []:
		return 0
	return len(s[-1])
	
	
if __name__ == "__main__":
	s = "Hello World"
	#s = " "
	#s = "a "
	print(lengthOfLastWord(s))
	
#Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

#A word is a maximal substring consisting of non-space characters only.


#Example 1:

#Input: s = "Hello World"
#Output: 5
#Example 2:

#Input: s = " "
#Output: 0