def integerReplacement(n):
	#int to count no of operations
	count = 0
	
	
	while n > 1:
		#print(f"n: {n}")
		#Edge Case: if n == 3: then our logic would do operations as 3 -> 4 -> 2 -> 1 but actually it should do 3 -> 2 -> 1
		if n == 3:
			count += 2
			break
		
		#base case
		if n % 2 == 0:
			n = n // 2
			
		#test case: for example- if n == 15: then our logic would do 15 -> 16 -> 8 -> 4 -> 2 -> 1
		elif (n + 1) % 4 == 0:
			n += 1
		#test case: for example- if n == 17: then our logic would do 17 -> 16 -> 8 -> 4 -> 2 -> 1
		else:
			n -= 1
		
		#increment operation
		count += 1
		
	return count
		
if __name__ == "__main__":
	n = 8 #3 
	n = 7 #4
	n = 4 #2
	n = 1234 #2
	#n = 17
	n = 3
	print(integerReplacement(n))
	
	
	
	#17 -> 18 -> 9 -> 8
	
	#17 -> 16 -> 8
	
	#Edge Case - 3 -> 4 -> 2 -> 1
	#soln - 	 3 -> 2 -> 1
	
#Given a positive integer n, you can apply one of the following operations:

#If n is even, replace n with n / 2.
#If n is odd, replace n with either n + 1 or n - 1.
#Return the minimum number of operations needed for n to become 1.

 
#Example 1:

#Input: n = 8
#Output: 3
#Explanation: 8 -> 4 -> 2 -> 1

#Example 2:

#Input: n = 7
#Output: 4
#Explanation: 7 -> 8 -> 4 -> 2 -> 1
#or 7 -> 6 -> 3 -> 2 -> 1

#Example 3:

#Input: n = 4
#Output: 2	