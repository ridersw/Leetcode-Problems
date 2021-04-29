def maxNumberOfFamilies(n, reservedSeats):
	count = 0
	
	reservedSeatsMatrix = [ [0]*10 for i in range(n)]
	
	for swi in range(n):
		for swj in range(10):
			if [swi+1, swj+1] in reservedSeats:
				reservedSeatsMatrix[swi][swj] = 1
	
	for seats in reservedSeatsMatrix:
		print(f"{seats}")
	
	for swi in range(n):
		for swj in range(1, 6):
			if swj == 2:
				continue
			#print(f"Checking for swi: {swi} & swj: {swj}")
			if reservedSeatsMatrix[swi][swj] + reservedSeatsMatrix[swi][swj+1] + reservedSeatsMatrix[swi][swj+2] + reservedSeatsMatrix[swi][swj+3] == 0:
					count += 1
					print(f"[swi]   [swj]: {swi}   {swj}")
					reservedSeatsMatrix[swi][swj] = 1
					reservedSeatsMatrix[swi][swj+1] = 1
					reservedSeatsMatrix[swi][swj+2] = 1
					reservedSeatsMatrix[swi][swj+3] = 1
		
	
	return count
	
if __name__ == "__main__":
	n = 3
	reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
	
	n = 2
	reservedSeats = [[2,1],[1,8],[2,6]]
	
	#n = 4
	#reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
	
	n = 4
	reservedSeats = [[2,10],[3,1],[1,2],[2,2],[3,5],[4,1],[4,9],[2,7]]
	
	print(maxNumberOfFamilies(n, reservedSeats))
	
#A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, labelled from 1 to 10 as shown in the figure above.

#Given the array reservedSeats containing the numbers of seats already reserved, for example, reservedSeats[i] = [3,8] means the seat located in row 3 and labelled with 8 is already reserved.

#Return the maximum number of four-person groups you can assign on the cinema seats. A four-person group occupies four adjacent seats in one single row. Seats across an aisle (such as [3,3] and [3,4]) are not considered to be adjacent, but there is an exceptional case on which an aisle split a four-person group, in that case, the aisle split a four-person group in the middle, which means to have two people on each side.

 #Example 1:



#Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
#Output: 4
#Explanation: The figure above shows the optimal allocation for four groups, where seats mark with blue are already reserved and contiguous seats mark with orange are for one group.
#Example 2:

#Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
#Output: 2
#Example 3:

#Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
#Output: 4