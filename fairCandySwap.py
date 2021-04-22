def fairCandySwap(A, B):
	result = []
	changed = False
	
	diff = abs(sum(A) - sum(B)) // 2
	
	if sum(B) > sum(A):
		A, B = B, A
		changed = True
		
	
	
	for swi in range(len(A)):
		for swj in range(len(B)):
			if (A[swi] - B[swj]) == diff:
				result.append(A[swi])
				result.append(B[swj])
				if changed:
					result[0], result[1] = result[1], result[0]
					return result
				else:
					return result
			if (A[swi] - B[swj]) < diff:
				break

if __name__ == "__main__":
	A = [1,1]
	B = [2,2]
	
	A = [1,2]
	B = [2,3]
	
	A = [2]
	B = [1,3]
	
	A = [1,2,5]
	B = [2,4]
	
	print(fairCandySwap(A, B))
	
#Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

#Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

#Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

#If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

#Example 1:

#Input: A = [1,1], B = [2,2]
#Output: [1,2]
#Example 2:

#Input: A = [1,2], B = [2,3]
#Output: [1,2]
#Example 3:

#Input: A = [2], B = [1,3]
#Output: [2,3]
#Example 4:

#Input: A = [1,2,5], B = [2,4]
#Output: [5,4]