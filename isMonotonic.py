def isMonotonic(A):
	#aCopy = A.copy()
	#aCopy.sort()
	
	#if aCopy != A:
	#	aCopy.sort(reverse = True)
	#	if aCopy != A:
	#		return False
			
	#return True
	return A == sorted(A) or A[::-1] == sorted(A) 
	
if __name__ == "__main__":
	A = [6,5,4,4]
	print(isMonotonic(A))
	
#An array is monotonic if it is either monotone increasing or monotone decreasing.

#An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

#Return true if and only if the given array A is monotonic.

#Example 1:

#Input: [1,2,2,3]
#Output: true
#Example 2:

#Input: [6,5,4,4]
#Output: true
#Example 3:

#Input: [1,3,2]
#Output: false