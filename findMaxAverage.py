def findMaxAverage(nums, k):
	i = 1
	stop = len(nums) - k
	stored_sum = sum(nums[:k])
	avg = stored_sum
	while i <= stop:
		stored_sum = stored_sum - nums[i-1] + nums[i+k-1]
		if stored_sum > avg:
			avg = stored_sum
		i = i + 1
	return avg/k
	
if __name__ == "__main__":
	print(findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
	print(findMaxAverage(nums = [5], k = 1))
	print(findMaxAverage(nums = [0,1,1,3,3], k = 4))
	
	
#You are given an integer array nums consisting of n elements, and an integer k.

#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.