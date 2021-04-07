def secondHighest(s):
	#alphabets = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','z','x','c','v','b','n','m']
	#print(f"s: {s}")
	numbersCollection = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	
	s = list(s)
	
	s.sort()
	
	#print(f"s: {s}")
	
	numbers = []
	
	for char in s:
		if char in numbersCollection:
			if int(char) not in numbers:
				numbers.append(int(char))
		else:
			break
			
	if len(numbers) >= 2:
		numbers.sort(reverse = True)
		return numbers[1]
	else:
		return -1
	
	
if __name__ == "__main__":
	string = 'abc1111456'
	print(secondHighest(string))
	
#Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

#An alphanumeric string is a string consisting of lowercase English letters and digits.

 

#Example 1:

#Input: s = "dfa12321afd"
#Output: 2
#Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

#Example 2:

#Input: s = "abc1111"
#Output: -1
#Explanation: The digits that appear in s are [1]. There is no second largest digit. 