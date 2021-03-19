def longestCommonPrefix(strs):
	prefix = ""
	
	strs = sorted(strs, key =len)
	
	letter = list(strs[0])
	
	swi = 0
	match = True
	
	if len(letter) < 1:
		return ""
	
	while swi < len(letter) and match == True:
		for word in strs:
			#print(f"Comparing {word[swi]} and {letter[swi]}")
			if word[swi] != letter[swi]:
				#print("Mismatch Found")
				match = False
				break
		
		if match == False:
			break
		else:
			swi += 1
	return "".join(letter[:swi])
	
if __name__ == "__main__":
	strs = ["flower","flow","flight"]
	#strs = ["dog","racecar","car"]
	#strs = ["shashiraj","shashi",""]
	
	result = longestCommonPrefix(strs)
	print("Result: ", result)
	
	
#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".

 

#Example 1:

#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:

#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
 

#Constraints:

#0 <= strs.length <= 200
#0 <= strs[i].length <= 200
#strs[i] consists of only lower-case English letters.