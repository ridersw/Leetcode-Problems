class solution:
	def intersection(self, nums1, nums2):
		result = []
        
		tempArray1 = []
		tempArray2 = []
        
		if len(nums1) > len(nums2):
			tempArray2 = nums1
			tempArray1 = nums2
		else:
			tempArray1 = nums1
			tempArray2 = nums2
            
		for ele in tempArray1:
			if ele in tempArray2 and  ele not in result:     
				result.append(ele)
                
		return result    
		
		
if __name__ == "__main__":
	nums1 = [4,9,5], nums2 = [9,4,9,8,4]
	obj = solution()

	print(obj.intersection(nums1, nums2))	

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.	