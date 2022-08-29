class Solution:
    def binarySearch(self, arr, ele):
        start = 0
        end = len(arr)-1
        
        while start <= end:
            mid = (start + end)//2

            if arr[mid] == ele:
                return mid

            if arr[mid] > ele:
                end = mid - 1
            else:
                start = mid + 1

        return -1



if __name__ == "__main__":
    obj = Solution()

    print(obj.binarySearch([-1,0,3,5,9,12],9))
    print(obj.binarySearch([-1,0,3,5,9,12],2))