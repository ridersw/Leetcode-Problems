class Solution:
    def fibo(self, n):
        
        if n <= 2:
            return 1
        
        return self.fibo(n-1) + self.fibo(n-2)


if __name__ == "__main__":
    obj = Solution()

    print(obj.fibo(10))


# 0 1 1 2 3 5 8 13 21 

