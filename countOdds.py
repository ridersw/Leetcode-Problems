import math


class Solution:
    def countOdds(self, low, high):
        if low % 2 == 0:
            return (high-low+1) // 2
        return (high-low) // 2 + 1

if __name__ == "__main__":
    obj = Solution()

    print(obj.countOdds(low = 3, high = 7))
    print(obj.countOdds(low = 8, high = 10))

        
        