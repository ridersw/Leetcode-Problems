class Solution:
    def onePasTwoSum(self, arr, target):
        dict = {}

        for swi in range(len(arr)):
            if (target - arr[swi]) in dict:
                return [dict[target - arr[swi]],swi]
            dict[arr[swi]] = swi


if __name__ == "__main__":
    obj = Solution()
    print(obj.onePasTwoSum(arr = [1,2,3,4,5,6], target = 3))