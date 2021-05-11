def countPrimes(n):
	count = 0
	
	def isPrime(num):
		prime = True
		
		for swj in range(2, num):
			if num % swj == 0:
				prime = False
				break
		
		return prime
		
		
	for swi in range(2, n):
		if isPrime(swi):
			count += 1
	
	return count
	
	
if __name__ == "__main__":
	print(countPrimes(10))
	#print(countPrimes(0))
	#print(countPrimes(1))
	#print(countPrimes(10000))
	
#Count the number of prime numbers less than a non-negative number, n