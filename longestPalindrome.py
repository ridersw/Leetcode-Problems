class Solution:
	def longestPalindrome(self, s):
		swi = 0
		swj = len(s)
		
		longestPal = ""
		
		for swi in range(int(len(s)/2)+1):
			print(f'Checking with letter: {s[swi]}')
			for swj in range(len(s)-1, int(len(s)/2)-1, -1):
				print(f's[swi]: {s[swi]} and s[swj]: {s[swj]}')
				if s[swi] == s[swj]:
					print(f's[swi] == s[swj]')
					temp = s[swi:swj+1]
					print(f'temp: {temp}')
					if temp == temp[::-1] and not longestPal:
						if len(temp) > len(longestPal):
							longestPal = temp
						
		return longestPal				
		
if __name__ == "__main__":
	s = "babad"
	s = "cbbd"
	s = "a"
	s = "ac"
	
	obj = Solution()
	
	print(obj.longestPalindrome(s))
	