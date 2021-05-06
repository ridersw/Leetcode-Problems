def checkIfExist(arr):
	
	newArr = set()
	
	for item in arr:
		if item * 2 in newArr or item / 2 in newArr:
			return True
		else:
			newArr.add(item)
	
	
	return False
	
	#s = set()
	#for i in arr: 
	#	if 2*i in s or i/2 in s:
	#		return True
	#	else:
	#		s.add(i)
	#return False
	
	
if __name__ == "__main__":
	print(checkIfExist([0,1]))
	print(checkIfExist([-10,12,-20,-8,15]))
	
#Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

#More formally check if there exists two indices i and j such that :

#i != j
#0 <= i, j < arr.length
#arr[i] == 2 * arr[j]