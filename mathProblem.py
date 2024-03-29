class Solution:
    def mathProblem(self, num):
        while True:
            print(f'Current Num: {num}')
            if num % 2 == 0:
                num = num // 2
            else:
                num = (num*3) + 1

            

if __name__ == "__main__":
    obj = Solution()

    print(obj.mathProblem(num = 3))
    print(obj.mathProblem(num = 21))
    print(obj.mathProblem(num = 101))
    print(obj.mathProblem(num = 100000000))
    print(obj.mathProblem(num = 2101010101010010010100101010))



# World's Toughest Problem also known as Collatz conjecture
# link - https://www.quantamagazine.org/why-mathematicians-still-cant-solve-the-collatz-conjecture-20200922/