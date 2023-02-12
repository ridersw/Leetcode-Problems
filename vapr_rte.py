class Solution:
    def function(self, vapor_rate):
        vapor_rate.sort()
        return  vapor_rate[-1] * vapor_rate[-2]


if __name__ == "__main__":
    obj = Solution()
    print(obj.function(vapor_rate=[8,0,5,3,9,6]))

# Encryption and Decryption