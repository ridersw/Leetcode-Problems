class Solution:
	def gridOfRobot(self, positions):
		
		numberOfRobots = positions[0].count(1)
		print(f'numberOfRobots: {numberOfRobots}')
	
		for swi in range(1, len(positions)):
			currentPosition = positions[swi-1]
			temp = positions[swi]
			#print(temp)
			
			for swj in range(len(temp)):
				#print(f'temp[swj]: {temp[swj]}')
				#print(f'currentPosition[swj-1]: {currentPosition[swj-1]}')
				if temp[swj] != currentPosition[swj-1] and temp[swj] != currentPosition[swj+1] or temp[swj] != currentPosition[swj]:
					robotNumber = numberOfRobots - temp[swj+1:].count(1)
					return f"Grid {positions} is not Valid. The Robot {robotNumber} is at wrong place"
					
					
					
					
		return f"Grid {positions} is Valid"			
		
		
if __name__ == "__main__":
	obj = Solution()

	#positions = [[1,0,0,1], [0,1,1,0]]
	positions = [[1,0,0,0,1], [1,0,1,0,0]]
	print(obj.gridOfRobot(positions))	
	
#Given the grid of robot positions, indicate if it is a valid time series for the number of robots specified if the robots can only travel upto 1 index further than their position 1 step before

#input format: an array of arrays, of which each index can be 0 or 1. 
#An index corresponds to the physical location which is either occupied by robot 