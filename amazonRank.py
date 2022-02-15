import numpy as np

class Solution:
    def amazon(self, rank):
        count = 0

        length = 2
        elements = []

        while length <= len(rank):
            print(f'For length: {length}')
            for swi in range(len(rank)-length + 1):
                temp = rank[swi:swi+length]
                temp.sort()
                flag = False
                print(f'checking for array: {temp}')
                for swj in range(1, len(temp)):
                    if temp[swj] - temp[swj-1] > 1:
                        print(f'Found Difference for: {temp}')
                        elements.append([temp[swj], temp[swj-1]])
                        count += 1

            length += 1

        return count

if __name__ == "__main__":
    obj= Solution()

    rank = [4, 1, 3, 2]
    rank = [3,1,2]
    rank = [1,2]
    rank = [2,1,5,3,4]
    rank = [1,4,7]

    print(obj.amazon(rank))

    