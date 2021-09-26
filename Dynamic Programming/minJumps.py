class Solution:
    def jump(self, nums):
        
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps	
		
		
if __name__ == "__main__":
	obj = Solution()

	nums = [2,3,1,1,4]
	
	# farthest = 4
	# current_jump_end = 2
	# jump = 1
	
	#nums = [2,3,0,1,4]	
	#nums = [3,2,1]
	#nums = [1,1,1,1]

	
	print(obj.jump(nums))