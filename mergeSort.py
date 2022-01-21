class Solution:
    def mergeSort(self, array):
        
        if len(array) <= 1:
            return array

        mid = len(array) //2

        left = array[:mid]
        right= array[mid:]

        left = self.mergeSort(left)
        right = self.mergeSort(right)

        return self.merge(left, right)

    def merge(self, arr1, arr2):
        sortedArray = []

        swi = swj = 0

        while swi < len(arr1) and swj < len(arr2):
            if arr1[swi] < arr2[swj]:
                sortedArray.append(arr1[swi])
                swi += 1
            else:
                sortedArray.append(arr2[swj])
                swj += 1

        if swi < len(arr1):
            while swi < len(arr1):
                sortedArray.append(arr1[swi])
                swi += 1

        if swj < len(arr2):
            while swj < len(arr2):
                sortedArray.append(arr2[swj])
                swj += 1

        return sortedArray


if __name__ == "__main__":
    obj = Solution()

    array = [9,8,7,6,5,4,3,2,1]

    print(obj.mergeSort(array))