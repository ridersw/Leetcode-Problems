def decrypt(code, k):
	updatedCode = []
	
	if k > 0 and abs(k) > len(code):
		k = k % len(code)
	elif k < 0 and abs(k) > len(code):
		k = -(k % len(code))
	
	if k == 0:
		return [0] * len(code)
		
	length = len(code)
	code = code * 3
	print(f"code: {code}")
	print(f"k: {k}")
	
	
	if k > 0:
		print("k is positive")
		for swi in range(length, length * 2):
			updatedCode.append(sum(code[swi+1:swi+1+k]))
	else:
		print("k is negative")
		for swi in range(length, length * 2):
			print(f"For {code[swi]} list is {code[swi+k:swi]}")
			updatedCode.append(sum(code[swi+k:swi]))
	
	return updatedCode
if __name__ == "__main__":
	#code = [5,7,1,4]
	#k = 3
	
	#code = [1,2,3,4]
	#k = 0
	
	code = [2,4,9,3]
	k = -2
	print(decrypt(code, k))
	
#You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

#To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

#If k > 0, replace the ith number with the sum of the next k numbers.
#If k < 0, replace the ith number with the sum of the previous k numbers.
#If k == 0, replace the ith number with 0.
#As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

#Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

#Example 1:

#Input: code = [5,7,1,4], k = 3
#Output: [12,10,16,13]
#Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
#Example 2:

#Input: code = [1,2,3,4], k = 0
#Output: [0,0,0,0]
#Explanation: When k is zero, the numbers are replaced by 0. 