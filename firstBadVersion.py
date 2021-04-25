def firstBadVersion(n):
	
	def isBadVersion(version):
		bad = 4
		return version == bad
		
	firstBound = 0
	lastBound = n-1
	mid = n // 2
	
	ans = True
	
	while firstBound <= lastBound:
		
		mid = firstBound + ((lastBound-firstBound) // 2)
		
		if isBadVersion(mid) == False:
			firstBound = mid + 1
		else:
			lastBound = mid - 1
			
	return firstBound

if __name__ == "__main__":
	n = 5
	print(firstBadVersion(n))
	
	
#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

#You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

#Example 1:

#Input: n = 5, bad = 4
#Output: 4
#Explanation:
#call isBadVersion(3) -> false
#call isBadVersion(5) -> true
#call isBadVersion(4) -> true
#Then 4 is the first bad version.
#Example 2:

#Input: n = 1, bad = 1
#Output: 1