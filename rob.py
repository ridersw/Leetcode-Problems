def rob(nums):
	#amount = []
	#amount.extend(nums)
	
	#if len(nums) < 3:
	#	return max(nums)
		
	#temp = 0
	#for swi in range(0, len(nums)-1, 2):
	#	print(f"swi: {nums[swi]}")
	#	temp += nums[swi]
	#	print(f"Updated temp: {temp}")
		
	#amount.append(temp)
	#temp = 0
	#print(f"amount: {amount}")
	#print("==================================")
	
	#for swi in range(1, len(nums), 2):
	#	print(f"swi: {nums[swi]}")
	#	temp += nums[swi]
	#	print(f"Updated temp: {temp}")
	#amount.append(temp)
	
	#print(f"amount: {amount}")
	
	#return max(amount)
	amountArray = []
	
	
	def cal(nums):
		tempNum = nums.copy()
		amount = 0
		while True:
			temp = tempNum.index(max(tempNum))
			amount += tempNum[temp]
			
			if temp != 0 and temp != len(tempNum)-1:
				tempNum[temp] = 0
				tempNum[temp+1] = 0
				tempNum[temp-1] = 0
			elif temp == len(tempNum)-1:
				tempNum[temp] = 0
				tempNum[temp-1] = 0
				tempNum[0] = 0
			else:
				tempNum[temp] = 0
				tempNum[temp+1] = 0
				tempNum[-1] = 0
				
			if sum(tempNum) == 0:
				return amount
	
	if len(nums) < 3:
		return max(nums)
		
	for swi in range(len(nums)):
		amountArray.append(cal(nums))
		temp = nums.index(max(nums))
		nums[temp] = 0
		
		
	print(f"amountArray: {amountArray}")
	
	
	return max(amountArray)
	
if __name__ == "__main__":
	nums = [2,3,2]
	
	#nums = [1,2,3,1]
	
	#nums = [0]
	
	#nums = [1,3,1,3,100]
	#nums = [1,1,1]
	
	nums = [2,2,4,3,2,5]
	print(rob(nums))
	
#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

#Example 1:

#Input: nums = [2,3,2]
#Output: 3
#Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
#Example 2:

#Input: nums = [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount you can rob = 1 + 3 = 4.
#Example 3:

#Input: nums = [0]
#Output: 0