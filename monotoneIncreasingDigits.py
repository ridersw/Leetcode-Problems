class Solution:
    def monotoneIncreasingDigits(self, n):
        if n < 10:
            return n

        array = []

        for _, num in enumerate(str(n)):
            array.append(int(num))

        # print(f'array: {array}')
        n = len(array)

        for swi in range(n-1, 0, -1):
            if array[swi] < array[swi-1]:
                array[swi-1] -= 1
                for i in range(swi,n):
                    array[i] = 9
        
		# Convert the list back to a number
        return int("".join([str(x) for x in array]))
                


if __name__  == "__main__":
    obj = Solution()
    #print(obj.monotoneIncreasingDigits(n = 1234))
    print(obj.monotoneIncreasingDigits(n = 10))

# An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

# Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.

 

# Example 1:

# Input: n = 10
# Output: 9
# Example 2:

# Input: n = 1234
# Output: 1234
# Example 3:

# Input: n = 332
# Output: 299
 

# Constraints:

# 0 <= n <= 109