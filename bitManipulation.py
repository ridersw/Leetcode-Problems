class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
            
        return a if a <= MAX_INT else ~(a ^ MASK)

        

if __name__ == "__main__":
    obj= Solution()
    print(obj.getSum(a = 3, b = 1))