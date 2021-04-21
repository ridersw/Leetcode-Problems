#11:53 -> Start
#12:11 -> End

def reverseOnlyLetters(S):
	newString = []
	
	S = list(S)
	tempS = S[::-1]
	
	for tS in tempS:
		if tS.isalpha():
			newString.append(tS)
			
	#print(f"tS: {newString}")
	
	for swi in range(len(S)):
		if S[swi].isalpha():
			pass
		else:
			temp = newString[swi:]
			newString = newString[:swi]
			newString.append(S[swi])
			newString.extend(temp)
			
	return "".join(newString)
if __name__ == "__main__":
	S = "ab-cd"
	S = "a-bC-dEf-ghIj"
	print(reverseOnlyLetters(S))
	
#Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 
#Example 1:

#Input: "ab-cd"
#Output: "dc-ba"
#Example 2:

#Input: "a-bC-dEf-ghIj"
#Output: "j-Ih-gfE-dCba"
#Example 3:

#Input: "Test1ng-Leet=code-Q!"
#Output: "Qedo1ct-eeLg=ntse-T!"