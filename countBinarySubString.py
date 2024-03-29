class Solution:
	def countBinarySubstrings(self, s):
		array = []

		count = 1

		for swi in range(1, len(s)):
			if s[swi] == s[swi-1]:
				count += 1
				
			else:
				array.append(count)
				count = 1
				
		array.append(count)	
				
		print(f'array: {array}')
		
		countOfSubstrings = 0
		
		for swi in range(1, len(array)):
			countOfSubstrings += min(array[swi-1], array[swi])
		
		return countOfSubstrings
		
if __name__ == "__main__":

	obj = Solution()

	s = "00110011"
	#s = "110001111000000"
	
	print(obj.countBinarySubstrings(s))

#Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

#Substrings that occur multiple times are counted the number of times they occur.

#Example 1:

#Input: s = "00110011"
#Output: 6
#Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
#Notice that some of these substrings repeat and are counted the number of times they occur.
#Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

#Example 2:

#Input: s = "10101"
#Output: 4
#Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.	