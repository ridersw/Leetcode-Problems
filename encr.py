class Solution:
    def function(self, s, n, m):
        # temp = (s**n)
        # if temp > 10:
        #     temp = temp % 10
        # temp = temp ** m
        # if temp > 1000000007:
        #     return temp % 1000000007
        # return temp

        # return pow(pow(s, n, 10) % 10, m, 1000000007)
        MOD = 1000000007
        ten_to_m = pow(10, m, MOD)
        return pow(s, n * ten_to_m, MOD)


if __name__ == "__main__":
    obj = Solution()
    print(obj.function(s = 2, n = 3, m = 4))

# Encryption and Decryption