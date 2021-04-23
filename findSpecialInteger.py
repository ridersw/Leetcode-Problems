def findSpecialInteger(arr):
	#size = len(arr) // 4
	#print(f"size: {size}")
	
	#newArr = arr.copy()
	#newArr = set(newArr)
	
	#for item in arr:
	#	if arr.count(item) > size:
	#		return item
	
	#return max(arr, key = arr.count)
	
	size = len(arr) // 4
	
	for swi in range(len(arr)):
		if arr[swi] == arr[swi+size]:
			return arr[swi]
	
	
if __name__ == "__main__":
	arr = [1,2,2,6,6,6,6,7,10]
	print(findSpecialInteger(arr))
	
	
#Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

#Example 1:

#Input: arr = [1,2,2,6,6,6,6,7,10]
#Output: 6
#Example 2:

#Input: arr = [1,1]
#Output: 1