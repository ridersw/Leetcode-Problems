class Solution:
    def denomination(self, arr, target):

        # if target == 0:
        #     return True

        # if target < 0:
        #     return False
        
        
        # for swi in range(len(arr)):
        #     remainderTarget = target - arr[swi]

        #     remain = self.denomination(arr, remainderTarget)

        #     if remain:
        #         return True

        # return False
        arr.sort()

        newArr = arr[::-1]

        for swi in range(len(newArr)):
            target = target % newArr[swi]

            if target == 0:
                return True

        return False

if __name__ == "__main__":
    obj = Solution()

    arr = [4,17,29]
    target = 75

    print(obj.denomination(arr, target))