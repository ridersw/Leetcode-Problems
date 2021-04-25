def isValid(s):
	if not s or len(s) % 2 != 0:
		return False
		
	while '()' in s or '{}' in s or '[]' in s:
		s = s.replace('()','')
		s = s.replace('{}','')
		s = s.replace('[]','')
		
	return s == ''
	
if __name__ == "__main__":
	s = "()"
	s = "()[]{}"
	s = "(]"
	print(isValid(s))
	
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
 
#Example 1:

#Input: s = "()"
#Output: true
#Example 2:

#Input: s = "()[]{}"
#Output: true
#Example 3:

#Input: s = "(]"
#Output: false
#Example 4:

#Input: s = "([)]"
#Output: false