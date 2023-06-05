class Solution:
    def removeItems(arr, number_of_items):
        for _ in range(len(number_of_items)):
            arr.remove(max(arr))

        return arr

if __name__ == "__main__":
    obj = Solution()
    print(obj.removeItems([[1,2,3,4,5,6,7,8,9]]))