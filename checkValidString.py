def checkValidString(s):
	
	high = 0
	low = 0
	
	for char in s:
		if char == '(':
			high += 1
			low += 1
		elif char == ')':
			high -= 1
			low -= 1
		else:
			high += 1
			low -= 1
			
		if high < 0:
			return False
		
		low = max(low, 0)
		
	return low == 0
		
	
	
if __name__ == "__main__":
	#s = "(*))"
	#s = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"
	s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
	print(checkValidString(s))
	
	
#Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

#The following rules define a valid string:

#Any left parenthesis '(' must have a corresponding right parenthesis ')'.
#Any right parenthesis ')' must have a corresponding left parenthesis '('.
#Left parenthesis '(' must go before the corresponding right parenthesis ')'.
#'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

#Example 1:

#Input: s = "()"
#Output: true
#Example 2:

#Input: s = "(*)"
#Output: true
#Example 3:

#Input: s = "(*))"
#Output: true