
class Solution:
    def sequentialDigits(self, low: int, high: int):
        sample = "123456789"
        n = 10
        
        result = []
        
        for length in range(len(str(low)), len(str(high))+1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    result.append(num)
                    
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.sequentialDigits(low = 100, high = 300))\

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]