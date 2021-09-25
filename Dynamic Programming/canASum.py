class Solution:
	def canASum(self, numbers, target, memo = {}):
		
		if target in memo:
			return memo[target]
		
		if target == 0:
			return []
			
		if target < 0:
			return None
		
		for num in numbers:
			remainder = target - num
			remainderArray = self.canASum(numbers, remainder)
			
			if remainderArray is not None:
				remainderArray.append(num)
				memo[target] = remainderArray 
				return memo[target]
		
		memo[target] = None	
		return memo[target]		

if __name__ == "__main__":
	numbers = [21, 3]
	target = 6300
	
	obj = Solution()
	print(obj.canASum(numbers, target))
	
#check if target can be acheived from elements in array	