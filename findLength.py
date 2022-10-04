class Solution:
    def findLength(self, nums1, nums2):
        result = 0

        for swi in range(len(nums2)):
            for swj in range(swi+1, len(nums2)):
                print(f'nums2: {nums2[swi:swj]} and nums1: {nums1} Ans: {nums2[swi:swj] in nums1}')
                if nums2[swi:swj] in nums2:
                    print(f'found: {nums2[swi:swj]}')
                    result = max(result, (swj-swi))

        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.findLength(nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]))