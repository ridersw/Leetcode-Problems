import numbers
from unicodedata import numeric


class Solution:
    def binary(self, S):
        
        # number = int(S, 2)
        # count = 0

        # # print(f'S: {number}')

        # while number > 0:
        #     if number % 2 == 0:
        #         number = number / 2
        #     else:
        #         number -= 1

        #     count += 1

        # return count

        # return S.count('1') + len(S) - 1

        # return S.count('1') * 2 + (len(S) - S.count('1') - 1) 

        return S.count('0') + (S.count('1')- 1) * 2 + 1


if __name__ == "__main__":
    obj = Solution()

    print(obj.binary('011100'))
    print(obj.binary('111'))