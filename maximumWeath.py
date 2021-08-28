#1 2 3
#3 2 1
#m = 2
#n = 3

class Solution:
	def maximumWealth(self, accounts):
	
		maxWealth = 0
		
		for wealth in accounts:
			if sum(wealth) > maxWealth:
				maxWealth = sum(wealth)
			
		return	maxWealth
		
if __name__ == "__main__":
	obj = Solution()
	
	accounts = [[1,2,3],[3,2,1]] 
	
	result = obj.maximumWealth(accounts)
	print(f"Maximum Wealth: {result}")	
	
#You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

#Example 1:

#Input: accounts = [[1,2,3],[3,2,1]]
#Output: 6
#Explanation:
#1st customer has wealth = 1 + 2 + 3 = 6
#2nd customer has wealth = 3 + 2 + 1 = 6
#Both customers are considered the richest with a wealth of 6 each, so return 6.	
