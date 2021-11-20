class Solution:
    def fizzbuzz(self, num):
        
        for swi in range(1, num+1):
            if swi % 5 == 0 and swi % 3 == 0:
                print("FizzBuzz")
            elif swi % 5 == 0 and swi % 3 != 0:
                print("Buzz")
            elif swi % 3 == 0 and swi % 5 != 0:
                print("Fizz")
            else:
                print(swi)

if __name__ == "__main__":
    obj = Solution()
    number = 15

    print(obj.fizzbuzz(number))