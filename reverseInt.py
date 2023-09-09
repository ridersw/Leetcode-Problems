class Solution:
    def reverse(self, x: int) -> int:
        result = list(str(x))
        if result[0] == "-":
            result = result[1:][::-1]
            result.insert(0,'-')
        else:
            result = result[::-1]
            
        
        result = ("".join(result))
        result = int(result)
        
        if result >= (2**31-1) or result <= (-2**31):
            return 0
        return result
        