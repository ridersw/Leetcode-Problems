def numWaterBottles(numBottles, numExchange):
	global count
	count = 0
	
	filled = numBottles
	empty = 0
	
	print(f"filled: {filled}")
	print(f"empty: {empty}")
	print("===========================")
	
	def countBottles(filled, empty, numExchange):
		global count
		count += filled
		if filled == 0 and empty < numExchange:
			return
	
		if filled > 0:
			empty += filled
			filled = 0
			print(f"filled: {filled}")
			print(f"empty: {empty}")
			print("===========================")
			
			return countBottles(filled, empty, numExchange)
		else:
			temp = empty
			filled = empty // numExchange
			empty = empty % numExchange
			print(f"Updated filled: {filled}")
			print(f"Updated empty: {empty}")
			print("===========================")
			return countBottles(filled, empty, numExchange)
			
	result = countBottles(filled, empty, numExchange)
	return count
	
if __name__ == "__main__":
	numBottles = 15
	numExchange = 4
	
	numBottles = 9
	numExchange = 3
	
	numBottles = 5
	numExchange = 5
	
	numBottles = 2
	numExchange = 3
	print(numWaterBottles(numBottles, numExchange))
	
#Given numBottles full water bottles, you can exchange numExchange empty water bottles for one full water bottle.

#The operation of drinking a full water bottle turns it into an empty bottle.

#Return the maximum number of water bottles you can drink.

#Example 1:

#Input: numBottles = 9, numExchange = 3
#Output: 13
#Explanation: You can exchange 3 empty bottles to get 1 full water bottle.
#Number of water bottles you can drink: 9 + 3 + 1 = 13.
#Example 2:

#Input: numBottles = 15, numExchange = 4
#Output: 19
#Explanation: You can exchange 4 empty bottles to get 1 full water bottle. 
#Number of water bottles you can drink: 15 + 3 + 1 = 19.