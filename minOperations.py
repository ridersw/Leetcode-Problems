def minOperations(s):
	if len(s) < 2:
		return 0
	
	tempS1 = []
	tempS2 = []
	countS1 = 0
	countS2 = 0
	
	for swi in range(len(s)):
		tempS1.append(str(swi % 2))
		if (swi % 2 == 0):
			tempS2.append("1")
		else:
			tempS2.append("0")
		
	print(f"tempS1: {tempS1}")
	print(f"tempS2: {tempS2}")
		
	for swi in range(len(s)):
		if s[swi] != tempS1[swi]:
			countS1 += 1
		if s[swi] != tempS2[swi]:
			countS2 += 1
			
	return min(countS1, countS2)
	
if __name__ == "__main__":
	s = "0100"
	#s = "10"
	#s = "1111"
	#s = "10010100"
	print(minOperations(s))
	
	
#You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

#The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

#Return the minimum number of operations needed to make s alternating.

#Example 1:

#Input: s = "0100"
#Output: 1
#Explanation: If you change the last character to '1', s will be "0101", which is alternating.
#Example 2:

#Input: s = "10"
#Output: 0
#Explanation: s is already alternating.
#Example 3:

#Input: s = "1111"
#Output: 2
#Explanation: You need two operations to reach "0101" or "1010".