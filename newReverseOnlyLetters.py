class Solution:
	def reverseOnlyLetters(self, s):
		
		swi = 0
		swj = len(s)-1
		
		s = list(s)
		
		while swi < swj:
			#print(f'swi: {swi} and swj: {swj}')
			#print(f's[swi].isalpha: {s[swi].isalpha()} and s[swj].isalpha(): {s[swj].isalpha()} ')
			if s[swi].isalpha() and s[swj].isalpha() and s[swi] != s[swj]:
				#print(f'Swapping {s[swi]} and {s[swj]}')
				s[swi], s[swj] = s[swj], s[swi]
				swi += 1
				swj -= 1
			elif s[swi].isalpha() == False:# and s[swj].isalpha():
				##print(f'found s[swi] : {s[swi]}, incrementing s[swi]')
				swi += 1
			elif s[swj].isalpha() == False:# and s[swi].isalpha():
				#print(f'found s[swj] : {s[swj]}, incrementing s[swj]')
				swj -= 1
			else:
				#print(f'found s[swi] : {s[swi]} and {s[swj]}, incrementing both')
				swi += 1
				swj -= 1
				
		return "".join(s)		
		
		
if __name__ == "__main__":
	obj = Solution()
	
	s = "ab-cd"
	s = "a-bC-dEf-ghIj"
	s = "Test1ng-Leet=code-Q!"
	answer = "Qedo1ct-eeLg=ntse-T!"
	print(obj.reverseOnlyLetters(s) == answer)	
	
	
#Given a string s, reverse the string according to the following rules:

#All the characters that are not English letters remain in the same position.
#All the English letters (lowercase or uppercase) should be reversed.
#Return s after reversing it.

 

#Example 1:

#Input: s = "ab-cd"
#Output: "dc-ba"
#Example 2:

#Input: s = "a-bC-dEf-ghIj"
#Output: "j-Ih-gfE-dCba"
#Example 3:

#Input: s = "Test1ng-Leet=code-Q!"
#Output: "Qedo1ct-eeLg=ntse-T!"