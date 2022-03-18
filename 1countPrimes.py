class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0

        primes = [True] * n

        primes[0] = primes[1] = False

        for swi in range(2, int(n ** 0.5) + 1):
            if primes[swi]:
                primes[swi * swi: n:swi] = [False] * len(primes[swi * swi: n: swi])

        return sum(primes)

if __name__ == "__main__":
    obj = Solution()

    print(obj.countPrimes(n = 5))

# Given an integer n, return the number of prime numbers that are strictly less than n.

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106