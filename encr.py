class Solution:
    def function(self, s, n, m):
        temp = (((s**n) % 10) ** m)
        if temp > 1000000007:
            return temp % 1000000007
        return ((((s**n) % 10) ** m) % 1000000007)


if __name__ == "__main__":
    obj = Solution()
    print(obj.function(s = 2, n = 3, m = 4))

# Encryption and Decryption