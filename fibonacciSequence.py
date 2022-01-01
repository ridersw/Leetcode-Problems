class Solution:
	def fib(self, n, memo = {}):
		if n == 0:
			return 0
	
		if n <= 2:
			return 1
		
		if n in memo:
			return memo[n]
			
		memo[n] = self.fib(n-1) + self.fib(n-2)
		return memo[n]	
		
if __name__ == "__main__":
	n = 7

	obj = Solution()

	print(obj.fibo(n))	

#fibonacci sequence code