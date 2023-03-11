import numpy as np

class Solution:
    def validWordSquare(self, wordSquare):
        wordSquare = np.array(wordSquare)

        print(f'row 1: {wordSquare[0,:]}')


if __name__ == "__main__":
    obj = Solution()
    # print(obj.validWordSquare(wordSquare = ["abcd","bnrt","crmy","dtye"]))
    # print(obj.validWordSquare(wordSquare = ["abcd","bnrt","crmy","dtye"]))
    print(obj.validWordSquare(wordSquare = ["ball","area","read","lady"]))