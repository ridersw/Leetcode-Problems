def halvesAreAlike(str):
	vowels = ['a','e','i','o','u']#,'A','E','I','O','U']
	
	length = len(str) // 2
	str = str.lower()
	
	print(f"length: {length}")
	
	#str = list(str)
	#str1 = str[:length]
	#str2 = str[length:]
	
	count = 0
	
	for swi in range(length):
		print(f"Checking for str[swi]: {str[swi]}")
		if str[swi] in vowels:
			print(f"Checking for str[swi]: {str[swi]}")
			count += 1
		if str[swi+length] in vowels:
			print(f"Checking for str[swi+length]: {str[swi+length]}")
			count -= 1
	
	if count == 0:
		return True
	else:
		return False
	
	
if __name__ == "__main__":
	str = ["book", "textbook", "MerryChristmas", "AbCdEfGh", "Uo"]
	
	for strs in str:
		print(halvesAreAlike(strs))
		
#You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

#Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

#Return true if a and b are alike. Otherwise, return false.

 

#Example 1:

#Input: s = "book"
#Output: true
#Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.