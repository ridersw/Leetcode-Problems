class Solution:
	def groupThePeople(self, groupSizes):
		dict = {}
		
		for swi in range(len(groupSizes)):
			if groupSizes[swi] in dict:
				dict[groupSizes[swi]] += [swi]
			else:
				dict[groupSizes[swi]] = [swi]
				
		print(dict)		
		
		result = []

		for keys, values in dict.items():
			swk = 0
			while swk <= len(values):
				if values[swk:swk+keys]:
					result.append(values[swk:swk+keys])
					
				swk += keys
		
		return result
		
		#finalResult =  []

		#for arr in result:
		#	if arr:
		#		finalResult.append(arr)
		#		
		#return finalResult		
		
if __name__ == "__main__":
	obj = Solution()
	
	groupSizes = [3,3,3,3,3,1,3]
	groupSizes = [2,1,3,3,3,2]
	
	print(f'Result: {obj.groupThePeople(groupSizes)}')	
	
#There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

#You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

#Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.	