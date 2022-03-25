class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1 
        
        while left <= right:
            pivot = left + (right-left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
    
if __name__ == "__main__":
    obj = Solution()
    print(obj.search(nums = [-1,0,3,5,9,12], target = 9))