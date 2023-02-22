class Solution:
    def advantageCount(self, nums1, nums2):
        sortedA = sorted(nums1)
        sortedB = sorted(nums2)
        
        assigned = {b: [] for b in nums2}
        remaining = []
        
        swj = 0
        for a in sortedA:
            # print(f'checking for a: {a} and sortedB[swj]: {sortedB[swj]}')
            if a > sortedB[swj]:
                assigned[sortedB[swj]].append(a)
                swj += 1
            else:
                remaining.append(a)
            
            # print(f'assigned: {assigned} and remaining: {remaining}]')
        
        res = []
        for b in nums2:
            if assigned[b]:
                res.append(assigned[b].pop())
            else:
                res.append(remaining.pop())
                
        return res
                

if __name__ == "__main__":
    obj = Solution()
    # print(obj.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))
    print(obj.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))