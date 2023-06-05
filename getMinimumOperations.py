class Solution:
    def getMinimumOperation(self, arr, x, y):
        count = 0
        while (max(arr) >= 0):
            arr.sort()
            arr[-1] = arr[-1] - x
            for swi in range(len(arr)-1):
                arr[swi] -= y
            count += 1

        return count
            

if __name__ == "__main__":
    obj = Solution()
    print(obj.getMinimumOperation(arr = [3,4,1,7,6], x= 4, y=2))