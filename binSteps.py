class Solution:
    def numberOfSteps(self, num):
        numInt = int(num, 2)
        print(f'numInt: {numInt}')
        print(f'len(bin(numInt)[2:]) - 1: {len(bin(numInt)[2:]) - 1}')
        print(f'numInt.bit_count(): {numInt.bit_count()}')
        return len(bin(numInt)[2:]) - 1 + num.bit_count()


if __name__ == "__main__":
    obj = Solution()

    print(obj.numberOfSteps('011100'))
        