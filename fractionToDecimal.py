class Solution:
    def fractionToDecimal(self, numerator, denominator):
        
        num = str(numerator/ denominator)

        index_of_decimal= num.index('.')

        if len(num[index_of_decimal:]) <= 1:
            return num

        print(f'Len after deimal is more than 1')

        # repeating_string = 

if __name__ == "__main__":
    obj = Solution()

    numerator = 4
    denominator = 333

    print(obj.fractionToDecimal(numerator, denominator))