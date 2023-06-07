class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = list(str(bin(a)[2:]))
        b = list(str(bin(b)[2:]))
        c = list(str(bin(c)[2:]))
        maxLen = max(len(a), len(b), len(c))

        tempLen = maxLen - len(a)
        if tempLen > 0:
            tempA = ['0'] * tempLen
            tempA.extend(a)
            a = tempA

        tempLen = maxLen - len(b)
        if tempLen > 0:
            tempB = ['0'] * tempLen
            tempB.extend(b)
            b = tempB

        tempLen = maxLen - len(c)
        if tempLen > 0:
            tempC = ['0'] * tempLen
            tempC.extend(c)
            c = tempC

        print(f'a: {a}')
        print(f'b: {b}')
        print(f'c: {c}')
        
        numberOfFlips = 0
        
        for swi in range(len(c)):
            if c[swi] == "0":
                if a[swi] == "1":
                    numberOfFlips += 1
                 
                if b[swi] == "1":
                    numberOfFlips += 1
            else: #if c[swi] == "1"
                 if a[swi] == "0" and b[swi] == "0":
                    numberOfFlips += 1
                 
        return numberOfFlips
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.minFlips(a = 8, b = 3, c = 5))

# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

 

# Example 1:



# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# Example 2:

# Input: a = 4, b = 2, c = 7
# Output: 1
# Example 3:

# Input: a = 1, b = 2, c = 3
# Output: 0
 

# Constraints:

# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9