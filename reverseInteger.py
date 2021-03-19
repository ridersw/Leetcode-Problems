def reverse(x: int) -> int:
	
	tempStr = str(x)
	
	if tempStr[0] == "-":
		tempStr = tempStr[1:]
	
	tempStr = tempStr[::-1]
	tempStr = "-" + tempStr
	x = int(tempStr)
	
	if x < -2 ** 31 or x > 2 ** 31 - 1:
		return 0
	else:	
		return int(tempStr)
	
if __name__ == "__main__":
	x = -123
	result = reverse(x)
	print("Result: ", result)
	
	
	
	
	
#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

#Example 1:

#Input: x = 123
#Output: 321
#Example 2:

#Input: x = -123
#Output: -321

#Constraints:

#-2^31 <= x <= 2^31 - 1