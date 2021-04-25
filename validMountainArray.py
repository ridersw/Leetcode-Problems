def validMountainArray(arr):

	if len(set(arr)) < 3:
		return False
		
	#for swi in range(len(arr)-1):
	#	if arr[swi] == arr[swi+1]:
	#		return False
	
	peakElement = max(arr)
	indexMaxElement = arr.index(peakElement)
	
	if indexMaxElement == 0 or indexMaxElement == len(arr)-1:
		return False
	
	for swi in range(indexMaxElement-1):
		if arr[swi] >= arr[swi+1]:
			return False
		
	for swi in range(indexMaxElement, len(arr)-1):
		if arr[swi] <= arr[swi+1]:
			return False
			
	return True
	
if __name__ == "__main__":
	arr = [0,2,3,4,5,2,1,0]
	arr = [2,1]
	arr = [3,5,5]
	arr = [0,3,2,1]
	arr = [0,1,2,3,4,5,6,7,8,9]
	arr = [9,8,7,6,5,4,3,2,1,0]
	arr = [1,3,2]
	print(validMountainArray(arr))
	
	
#Given an array of integers arr, return true if and only if it is a valid mountain array.

#Recall that arr is a mountain array if and only if:

#arr.length >= 3
#There exists some i with 0 < i < arr.length - 1 such that:
#arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


#Example 1:

#Input: arr = [2,1]
#Output: false
#Example 2:

#Input: arr = [3,5,5]
#Output: false
#Example 3:

#Input: arr = [0,3,2,1]
#Output: true