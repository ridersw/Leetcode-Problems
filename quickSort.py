class Solution:
    def quickSort(self, array, low, high):
        if len(array) == 1:
            return array

        if low < high:



if __name__ == "__main__":
    obj = Solution()

    array = [10, 7, 8, 9, 1, 5]

    print(obj.quickSort(array, 0, len(array)-1))