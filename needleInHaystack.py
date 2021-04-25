def strStr(haystack, needle):
	if not needle:
		return 0

	#if needle not in haystack:
	#	return -1
	#else:
	#	return haystack.index(needle)
	
	if needle in haystack:
		return haystack.index(needle)
	return -1
	
if __name__ == "__main__":
	haystack = "hello"
	needle = "ll"
	
	haystack = "aaaaa"
	needle = "bba"
	
	#haystack = ""
	#needle = ""
	print(strStr(haystack, needle))
	
#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#Clarification:

#What should we return when needle is an empty string? This is a great question to ask during an interview.

#For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

#Example 1:

#Input: haystack = "hello", needle = "ll"
#Output: 2
#Example 2:

#Input: haystack = "aaaaa", needle = "bba"
#Output: -1
#Example 3:

#Input: haystack = "", needle = ""
#Output: 0