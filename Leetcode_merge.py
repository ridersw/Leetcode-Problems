class Solution:
    def merge(self, nums1, m, nums2, n):
        
        nums1 = nums1[:m]
        nums1.extend(nums2)
        print(nums1)
        nums1.sort()
        return nums1


if __name__ == "__main__":
    obj = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    print(obj.merge(nums1, m, nums2, n))