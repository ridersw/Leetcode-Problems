def arrangeCoins(n: int) -> int:
	
	count = 1

	while True:
		#print(f"Value of n: {n}")
		n -= count
		if n >= 0:
			count+= 1
		else:
			return count-1
	
if __name__ == "__main__":
	print(arrangeCoins(n = 8))
	print(arrangeCoins(n = 5))
	
#You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

#Given the integer n, return the number of complete rows of the staircase you will build.