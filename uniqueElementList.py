class Solution:
    def unique(self, numbers):
        tempList = set()
        finalList = []

        for num in numbers:
            if num not in tempList:
                finalList.append(num)
                tempList.add(num)

        return list(tempList)

if __name__ == "__main__":
    obj = Solution()
    
    print(obj.unique([1, 2, 3, 2, 4, 5, 1, 3, 6]))